def calculate_steady_state_temp(T_a,tau):
    T_w=323
    while True:
        T_m=(T_a+T_w)/2
        B=1.32 -(1.2*0.001*(T_m-293))
        i=0.561*B*tau
        R=0.0575*(1+(0.0039*(T_w-293)))
        P_c=3*i*i*R
        P_e=9.602*pow(10,-6)*(pow(B*tau,2))/R
        new=T_a+(0.455*(P_c+P_e))
        if(abs(new-T_w))<1:
            return new
        T_w=new
        print(T_w)

print(calculate_steady_state_temp(303,35))