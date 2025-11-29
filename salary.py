import sys
if len(sys.argv)==5:
    script_name = sys.argv[0]
    HRA = sys.argv[1]
    TA = sys.argv[2]
    DA =  sys.argv[3]
    SALARY = sys.argv[4]
else:
    script_name = sys.argv[0]
    HRA = 1000.0
    TA = 1000.0
    DA = 1000.0
    SALARY = 50000.0
    Total =(float(HRA)+float(TA)+float(DA)+float(SALARY))
    print("using defult arguments")
    print("Gross salary =",Total)