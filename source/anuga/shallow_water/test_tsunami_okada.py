import unittest
from Numeric import allclose
from tsunami_okada import earthquake_tsunami,Okada_func

class Test_eq(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def NOtest_Okada_func(self):
        from os import sep, getenv
        from Numeric import zeros, Float,allclose
        import sys
        from anuga.abstract_2d_finite_volumes.mesh_factory import rectangular_cross
        from anuga.shallow_water import Domain
        from anuga.abstract_2d_finite_volumes.quantity import Quantity
        from anuga.utilities.system_tools import get_pathname_from_package
        """
        Pick the test you want to do; T= 0 test a point source,
        T= 1  test single rectangular source, T= 2 test multiple
        rectangular sources
        """
        #get path where this test is run
        path= get_pathname_from_package('anuga.shallow_water')
        #choose what test to proceed
        T=1
        


        if T==0:
            # fotran output file
            
            filename = path+sep+'fullokada_SP.txt'
        # initial condition of earthquake for multiple source
            x0 = 7000.0
            y0 = 10000.0
            length = 0
            width =0
            strike = 0.0
            depth = 15.0
            slip = 10.0
            dip =15.0
            rake =90.0
            ns=1
            NSMAX=1
        elif T==1:
        # fotran output file
            filename = path+sep+'fullokada_SS.txt'
        # initial condition of earthquake for multiple source
            x0 = 50000.0
            y0 = 25000.0
            length = 50.0
            width =10.0
            strike = 0.0
            depth = 10.0
            slip = 30.0
            dip =15.0
            rake =90.0
            ns=1
            NSMAX=1
            
        elif T==2:

        # fotran output file
            filename = path+sep+'fullokada_MS.txt'
        # initial condition of earthquake for multiple source
            x0 = [7000.0,10000.0]
            y0 = [10000.0,7000.0]
            length = [10.0,10.0]
            width =[6.0,6.0]
            strike = [0.0,0.0]
            depth = [15.0,15.0]
            slip = [10.0,10.0]
            dip = [15.0,15.0]
            rake = [90.0,90.0]
            ns=2
            NSMAX=2



        # get output file from original okada fortran script.
        # vertical displacement is listed under tmp.
        polyline_file=open(filename,'r')
        lines=polyline_file.readlines()
        polyline_file.close()
        tmp=[]
        stage=[]
        for line in lines [0:]:
            field = line.split('    ')
            z=float(field[2])
            tmp.append(z)

        

                
        #create domain 
        dx = dy = 4000
        l=100000
        w=100000
        #create topography
        def topography(x,y):
            el=-1000
            return el
        
        points, vertices, boundary = rectangular_cross(int(l/dx), int(w/dy),
                                               len1=l, len2=w)
        domain = Domain(points, vertices, boundary)   
        domain.set_name('test')
        domain.set_quantity('elevation',topography)
        
        #create variable with elevation data to implement in okada
        zrec0 = Quantity(domain)
        zrec0.set_values(0.0)
        zrec=zrec0.get_vertex_values(xy=True)
        # call okada
        Ts= Okada_func(ns=ns, NSMAX=NSMAX,length=length, width=width, dip=dip, \
                       x0=x0, y0=y0, strike=strike, depth=depth, \
                       slip=slip, rake=rake,zrec=zrec)

        #create a variable to store vertical displacement throughout the domain
        tsunami = Quantity(domain)
        tsunami.set_values(Ts)

        # get vertical displacement at each point of the domain respecting
        # original script's order
        k=0.0
        for i in range(0,6):
            for j in range(0,6):
                p=j*4000
                Yt=p
                Xt=k
                Z=tsunami.get_values(interpolation_points=[[Xt,Yt]]
                                     ,location='edges')
                stage.append(-Z[0])
            k=k+4000
        
        assert allclose(stage,tmp,atol=1.e-8)
        print stage
        print tmp
        print 'c est fini'

    def test_earthquake_tsunami(self):
        from os import sep, getenv
        from Numeric import zeros, Float,allclose
        import sys
        from anuga.abstract_2d_finite_volumes.mesh_factory import rectangular_cross
        from anuga.shallow_water import Domain
        from anuga.abstract_2d_finite_volumes.quantity import Quantity
        from anuga.utilities.system_tools import get_pathname_from_package
        """
        Pick the test you want to do; T= 0 test a point source,
        T= 1  test single rectangular source, T= 2 test multiple
        rectangular sources
        """

        #get path where this test is run
        path= get_pathname_from_package('anuga.shallow_water')
        
        #choose what test to proceed
        T=1

        if T==0:
        # fotran output file
            
            filename = path+sep+'fullokada_SP.txt'
        # initial condition of earthquake for multiple source
            x0 = 7000.0
            y0 = 10000.0
            length = 0
            width =0
            strike = 0.0
            depth = 15.0
            slip = 10.0
            dip =15.0
            rake =90.0
            ns=1
            NSMAX=1
        elif T==1:
        # fotran output file
            filename = path+sep+'fullokada_SS.txt'
        # initial condition of earthquake for multiple source
            x0 = 7000.0
            y0 = 10000.0
            length = 10.0
            width =6.0
            strike = 0.0
            depth = 15.0
            slip = 10.0
            dip =15.0
            rake =90.0
            ns=1
            NSMAX=1
            
        elif T==2:

        # fotran output file
            filename = path+sep+'fullokada_MS.txt'
        # initial condition of earthquake for multiple source
            x0 = [7000.0,10000.0]
            y0 = [10000.0,7000.0]
            length = [10.0,10.0]
            width =[6.0,6.0]
            strike = [0.0,0.0]
            depth = [15.0,15.0]
            slip = [10.0,10.0]
            dip = [15.0,15.0]
            rake = [90.0,90.0]
            ns=2
            NSMAX=2



        # get output file from original okada fortran script.
        # vertical displacement is listed under tmp.
        polyline_file=open(filename,'r')
        lines=polyline_file.readlines()
        polyline_file.close()
        tmp=[]
        stage=[]
        for line in lines [0:]:
            field = line.split('    ')
            z=float(field[2])
            tmp.append(z)

         
        # Create domain 
        dx = dy = 4000
        l=20000
        w=20000
        
        # Create topography
        def topography(x,y):
            el=-1000
            return el
        
        points, vertices, boundary = rectangular_cross(int(l/dx), int(w/dy),
                                               len1=l, len2=w)
        domain = Domain(points, vertices, boundary)   
        domain.set_name('test')
        domain.set_quantity('elevation',topography)
        Ts = earthquake_tsunami(ns=ns,NSMAX=NSMAX,length=length, width=width, strike=strike,\
                                depth=depth,dip=dip, xi=x0, yi=y0,z0=0, slip=slip, rake=rake,\
                                domain=domain, verbose=False)
        
        # Create a variable to store vertical displacement throughout the domain
        tsunami = Quantity(domain)
        tsunami.set_values(Ts)

        #k=0.0
        #for i in range(0,6):
        #    for j in range(0,6):
        #        p=j*4000
        #        Yt=p
        #        Xt=k
        #        Z=tsunami.get_values(interpolation_points=[[Xt,Yt]]
        #                             ,location='edges')
        #        stage.append(-Z[0])
        #    k=k+4000
        #
        #assert allclose(stage,tmp,atol=1.e-3)

        # Here's a faster way - try that in the first test
        interpolation_points=[]
        k=0.0
        for i in range(0,6):
            for j in range(0,6):
                p=j*4000
                Yt=p
                Xt=k
                interpolation_points.append([Xt, Yt])

            k=k+4000

        Z=tsunami.get_values(interpolation_points=interpolation_points,
                             location='edges')

        stage = -Z # FIXME(Ole): Why the sign flip?
        
        assert allclose(stage, tmp, atol=1.e-3)

#-------------------------------------------------------------
if __name__ == "__main__":
    #suite = unittest.makeSuite(Test_eq,'test_Okada_func')
    suite = unittest.makeSuite(Test_eq,'test')
    runner = unittest.TextTestRunner()
    runner.run(suite)

