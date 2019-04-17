#include <assert.h>
#include <float.h>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#ifdef HAVE_FEENABLEEXCEPT
#define _GNU_SOURCE
#include <fenv.h>
#if 0
#include "fe-handling-example.c"
#endif
#endif

#include <ostream>
#include <sstream>
#include <iostream>

using std::ostream;


class Double {
  public:
    static int nadds;
    static int nmults;
    static int ndivs;
    static std::size_t nbytes;
    static void *operator new(std::size_t sz) { Double::nbytes += sz; return ::operator new(sz); };
    static void *operator new[](std::size_t sz) { Double::nbytes += sz; return ::operator new(sz); };
    double x;
    inline Double() : x(0) {};
    inline Double(double _x) : x(_x) {};
    inline Double(int _x) : x((double) _x) {};
    inline Double &operator=(const Double& rhs) { this->x = rhs.x; return *this; };
    inline operator double() const { return x; };
};

inline Double operator+(const Double& lhs, const Double& rhs) {  Double::nadds++; return lhs.x + rhs.x; };
inline Double operator+(const int& lhs, const Double& rhs) {  Double::nadds++; return lhs + rhs.x; };
inline Double operator+(const Double& lhs, const int& rhs) {  Double::nadds++; return lhs.x + rhs; };
inline Double operator+(const double& lhs, const Double& rhs) {  Double::nadds++; return lhs + rhs.x; };
inline Double operator+(const Double& lhs, const double& rhs) {  Double::nadds++; return lhs.x + rhs; };
inline Double operator+=(Double& lhs, const Double& rhs) {  Double::nadds++; return lhs.x += rhs.x; };
inline Double operator-(const Double& lhs, const Double& rhs) {  Double::nadds++; return lhs.x - rhs.x; };
inline Double operator-(const int& lhs, const Double& rhs) {  Double::nadds++; return lhs - rhs.x; };
inline Double operator-(const Double& lhs, const int& rhs) {  Double::nadds++; return lhs.x - rhs; };
inline Double operator-(const double& lhs, const Double& rhs) {  Double::nadds++; return lhs - rhs.x; };
inline Double operator-(const Double& lhs, const double& rhs) {  Double::nadds++; return lhs.x - rhs; };
inline Double operator-(const Double& rhs) {  Double::nadds++; return -rhs.x; };
inline Double operator-=(Double& lhs, const Double& rhs) {  Double::nadds++; return lhs.x -= rhs.x; };
inline Double operator*(const Double& lhs, const Double& rhs) { Double::nmults++; return lhs.x * rhs.x; };
inline Double operator*(const int& lhs, const Double& rhs) { Double::nmults++; return lhs * rhs.x; };
inline Double operator*(const Double& lhs, const int& rhs) { Double::nmults++; return lhs.x * rhs; };
inline Double operator*(const double& lhs, const Double& rhs) { Double::nmults++; return lhs * rhs.x; };
inline Double operator*(const Double& lhs, const double& rhs) { Double::nmults++; return lhs.x * rhs; };
inline Double operator*=(Double& lhs, const Double& rhs) { Double::nmults++; return lhs.x *= rhs.x; };
inline Double operator/(const Double& lhs, const Double& rhs) { Double::ndivs++; return lhs.x / rhs.x; };
inline Double operator/(const int& lhs, const Double& rhs) { Double::ndivs++; return lhs / rhs.x; };
inline Double operator/(const Double& lhs, const int& rhs) { Double::ndivs++; return lhs.x / rhs; };
inline Double operator/(const double& lhs, const Double& rhs) { Double::ndivs++; return lhs / rhs.x; };
inline Double operator/(const Double& lhs, const double& rhs) { Double::ndivs++; return lhs.x / rhs; };
inline Double operator/=(Double& lhs, const Double& rhs) { Double::ndivs++; return lhs.x /= rhs.x; };
inline bool operator< (const Double& lhs, const Double& rhs){ return lhs.x < rhs.x; }
inline bool operator< (const int& lhs, const Double& rhs){ return lhs < rhs.x; }
inline bool operator< (const Double& lhs, const int& rhs){ return lhs.x < rhs; }
inline bool operator< (const double& lhs, const Double& rhs){ return lhs < rhs.x; }
inline bool operator< (const Double& lhs, const double& rhs){ return lhs.x < rhs; }
inline bool operator> (const Double& lhs, const Double& rhs){ return rhs < lhs; }
inline bool operator> (const int& lhs, const Double& rhs){ return rhs < lhs; }
inline bool operator> (const Double& lhs, const int& rhs){ return rhs < lhs; }
inline bool operator> (const double& lhs, const Double& rhs){ return rhs < lhs; }
inline bool operator> (const Double& lhs, const double& rhs){ return rhs < lhs; }
inline bool operator<=(const Double& lhs, const Double& rhs){ return !(lhs > rhs); }
inline bool operator<=(const int& lhs, const Double& rhs){ return !(lhs > rhs); }
inline bool operator<=(const Double& lhs, const int& rhs){ return !(lhs > rhs); }
inline bool operator<=(const double& lhs, const Double& rhs){ return !(lhs > rhs); }
inline bool operator<=(const Double& lhs, const double& rhs){ return !(lhs > rhs); }
inline bool operator>=(const Double& lhs, const Double& rhs){ return !(lhs < rhs); }
inline bool operator>=(const int& lhs, const Double& rhs){ return !(lhs < rhs); }
inline bool operator>=(const Double& lhs, const int& rhs){ return !(lhs < rhs); }
inline bool operator>=(const double& lhs, const Double& rhs){ return !(lhs < rhs); }
inline bool operator>=(const Double& lhs, const double& rhs){ return !(lhs < rhs); }
inline bool operator==(const Double& lhs, const Double& rhs){ return lhs.x == rhs.x; }
inline bool operator==(const int& lhs, const Double& rhs){ return lhs == rhs.x; }
inline bool operator==(const Double& lhs, const int& rhs){ return lhs.x == rhs; }
inline bool operator==(const double& lhs, const Double& rhs){ return lhs == rhs.x; }
inline bool operator==(const Double& lhs, const double& rhs){ return lhs.x == rhs; }
inline bool operator!=(const Double& lhs, const Double& rhs){ return !(lhs == rhs); }
inline bool operator!=(const int& lhs, const Double& rhs){ return !(lhs == rhs); }
inline bool operator!=(const Double& lhs, const int& rhs){ return !(lhs == rhs); }
inline bool operator!=(const double& lhs, const Double& rhs){ return !(lhs == rhs); }
inline bool operator!=(const Double& lhs, const double& rhs){ return !(lhs == rhs); }
inline ostream& operator<<(ostream& os, const Double& rhs)  { os << rhs.x; return os; }

int Double::nadds = 0;
int Double::nmults = 0;
int Double::ndivs = 0;
std::size_t Double::nbytes = 0;

int const Nt_max = 50000;
int const Nx_max = 10000;

int noout = 0;
int savi = 0;
int outi = 100;
int save = 0;
char const *alg = "ftcs";
char const *prec = "double";
char const *ic = "const(1)";
Double lenx = 1.0;
Double alpha = 0.2;
Double dt = 0.004;
Double dx = 0.1;
Double bc0 = 0;
Double bc1 = 1;
Double maxt = 2.0;

Double *curr=0, *last=0, *change_history=0, *exact=0, *error_history=0;
Double *cn_Amat = 0;

int Nx = (int) (lenx/dx);
int Nt = (int) (maxt/dt);

/*
 * Utilities 
 */
static Double
l2_norm(int n, Double const *a, Double const *b)
{
    int i;
    Double sum = 0;
    for (i = 0; i < n; i++)
    {
        Double diff = a[i] - b[i];
        sum += diff * diff;
    }
    return sum;
}

static void
copy(int n, Double *dst, Double const *src)
{
    int i;
    for (i = 0; i < n; i++)
        dst[i] = src[i];
}

#define TSTART -1
#define TFINAL -2
#define RESIDUAL -3
#define ERROR -4
static void
write_array(int t, int n, Double dx, Double const *a)
{
    int i;
    char fname[32];
    FILE *outf;

    if (noout) return;

    if (t == TSTART)
        snprintf(fname, sizeof(fname), "heat_soln_00000.curve");
    else if (t == TFINAL)
        snprintf(fname, sizeof(fname), "heat_soln_final.curve");
    else if (t == RESIDUAL)
        snprintf(fname, sizeof(fname), "change.curve");
    else if (t == ERROR)
        snprintf(fname, sizeof(fname), "error.curve");
    else
    {
        if (a == exact)
            snprintf(fname, sizeof(fname), "heat_exact_%05d.curve", t);
        else
            snprintf(fname, sizeof(fname), "heat_soln_%05d.curve", t);
    }
    
    outf = fopen(fname,"w");
    for (i = 0; i < n; i++)
        fprintf(outf, "%8.4g %8.4g\n", i*dx.x, a[i].x);
    fclose(outf);
}


static void
r83_np_fa(int n, Double *a)
/*
  Licensing: This code is distributed under the GNU LGPL license. 
  Modified: 30 May 2009 Author: John Burkardt
  Modified by Mark C. Miller, July 23, 2017
*/
{
    int i;

    for ( i = 1; i <= n-1; i++ )
    {
        assert ( a[1+(i-1)*3] != 0.0 );
        /*
          Store the multiplier in L.
        */
        a[2+(i-1)*3] = a[2+(i-1)*3] / a[1+(i-1)*3];
        /*
          Modify the diagonal entry in the next column.
        */
        a[1+i*3] = a[1+i*3] - a[2+(i-1)*3] * a[0+i*3];
    }

    assert( a[1+(n-1)*3] != 0.0 );
}

static void
initialize(void)
{
    curr = new Double[Nx]();
    last = new Double[Nx]();
    if (save)
    {
        exact = new Double[Nx]();
        change_history = new Double[Nx]();
        error_history = new Double[Nx]();
    }

    assert(strncmp(alg, "ftcs", 4)==0 ||
           strncmp(alg, "upwind15", 8)==0 ||
           strncmp(alg, "crankn", 6)==0);

#ifdef HAVE_FEENABLEEXCEPT
    feenableexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW);
#endif

    if (!strncmp(alg, "crankn", 6))
    {
        /*
          We do some additional initialization work for Crank-Nicolson.
          The matrix A does not change with time.  We can set it once,
          factor it once, and solve repeatedly.
        */
        int i;
        Double w = alpha * dt / dx / dx;

        cn_Amat = new Double[3*Nx]();

        cn_Amat[0+0*3] = 0.0;
        cn_Amat[1+0*3] = 1.0;
        cn_Amat[0+1*3] = 0.0;

        for ( i = 1; i < Nx - 1; i++ )
        {
            cn_Amat[2+(i-1)*3] =           - w;
            cn_Amat[1+ i   *3] = 1.0 + 2.0 * w;
            cn_Amat[0+(i+1)*3] =           - w;
        }
        
        cn_Amat[2+(Nx-2)*3] = 0.0;
        cn_Amat[1+(Nx-1)*3] = 1.0;
        cn_Amat[2+(Nx-1)*3] = 0.0;

        /*
          Factor the matrix.
        */
        r83_np_fa(Nx, cn_Amat);
    }
}

#define HANDLE_ARG(VAR, TYPE, STYLE, HELP) \
{ \
    char const *style = #STYLE; \
    char const *q = style[1]=='s'?"\"":""; \
    void *valp = (void*) &VAR; \
    int const len = strlen(#VAR)+1; \
    std::stringstream strmvar; \
    for (i = 1; i < argc; i++) \
    {\
        int valid_style = style[1]=='d'||style[1]=='g'||style[1]=='s'; \
        if (strncmp(argv[i], #VAR"=", len)) \
            continue; \
        assert(valid_style); \
	if (strlen(argv[i]+len)) \
        {\
            if      (style[1] == 'd') /* int */ \
                *((int*) valp) = (int) strtol(argv[i]+len,0,10); \
            else if (style[1] == 'g') /* double */ \
                *((Double*) valp) = (double) strtod(argv[i]+len,0); \
            else if (style[1] == 's') /* char* */ \
                *((char**) valp) = (char*) strdup(argv[i]+len); \
        }\
    }\
    strmvar << VAR; \
    if (help) \
    {\
        char tmp[256]; \
        int len = snprintf(tmp, sizeof(tmp), "        %s=%s%s%s", \
            #VAR, q, strmvar.str().c_str(), q);\
        snprintf(tmp, sizeof(tmp), "%s (%s)", #HELP, #TYPE); \
        fprintf(stderr, "        %s=%s%s%s%*s\n", \
            #VAR, q, strmvar.str().c_str(), q, 80-len, tmp);\
    }\
    else \
        fprintf(stderr, "    %s=%s%s%s\n", \
            #VAR, q, strmvar.str().c_str(), q);\
}

static void
process_args(int argc, char **argv)
{
    int i;
    int help = 0;

    /* quick pass for 'help' anywhere on command line */
    for (i = 0; i < argc && !help; i++)
        help = 0!=strcasestr(argv[i], "help");
    
    if (help)
    {
        fprintf(stderr, "Usage:\n");
        fprintf(stderr, "    ./heat <arg>=<value> <arg>=<value>...\n");
    }

    HANDLE_ARG(prec, char*, %s, precision half|float|double|quad);
    HANDLE_ARG(alpha, double, %g, material thermal diffusivity);
    HANDLE_ARG(lenx, double, %g, material length);
    HANDLE_ARG(dx, double, %g, x-incriment (best if lenx/dx->int));
    HANDLE_ARG(dt, double, %g, t-incriment);
    HANDLE_ARG(maxt, double, %g, max. time to run simulation to);
    HANDLE_ARG(bc0, double, %g, boundary condition @ x=0: u(0,t));
    HANDLE_ARG(bc1, double, %g, boundary condition @ x=1: u(1,t));
    HANDLE_ARG(ic, char*, %s, initial condition @ t=0: u(x,0));
    HANDLE_ARG(alg, char*, %s, algorithm ftcs|upwind15|crankn);
    HANDLE_ARG(savi, int, %d, save every i-th solution step);
    HANDLE_ARG(save, int, %d, save error in every saved solution);
    HANDLE_ARG(outi, int, %d, output progress every i-th solution step);
    HANDLE_ARG(noout, int, %d, disable all file outputs);

    if (help)
    {
        fprintf(stderr, "Examples...\n");
        fprintf(stderr, "    ./heat dx=0.01 dt=0.0002 alg=ftcs\n");
        fprintf(stderr, "    ./heat dx=0.1 bc0=5 bc1=10 ic=\"spikes(5,5)\"\n");
        exit(1);
    }

}

static void
set_initial_condition(int n, Double *a, Double dx, char const *ic)
{
    int i;
    Double x;

    if (!strncmp(ic, "const(", 6)) /* const(val) */
    {
        double cval = strtod(ic+6, 0);
        for (i = 0; i < n; i++)
            a[i] = cval;
    }
    else if (!strncmp(ic, "step(", 5)) /* step(left,xmid,right) */
    {
        char *p;
        double left = strtod(ic+5, &p);
        double xmid = strtod(p+1, &p);
        double right = strtod(p+1, 0);
        for (i = 0, x = 0; i < n; i++, x+=dx)
        {
            if (x < xmid) a[i] = left;
            else          a[i] = right;
        }
    }
    else if (!strncmp(ic, "ramp(", 5)) /* ramp(left,right) */
    {
        char *p;
        double left = strtod(ic+5, &p);
        double right = strtod(p+1, 0);
        double dv = (right-left)/(n-1);
        for (i = 0, x = left; i < n; i++, x+=dv)
            a[i] = x;
    }
    else if (!strncmp(ic, "rand(", 5)) /* rand(seed,amp) */
    {
        char *p;
        int seed = (int) strtol(ic+5,&p,10);
        double amp = strtod(p+1, 0);
        const double maxr = ((long long)1<<31)-1;
        srandom(seed);
        for (i = 0; i < n; i++)
            a[i] = amp * random()/maxr;
    }
    else if (!strncmp(ic, "sin(Pi*x)", 9)) /* rand(seed,amp) */
    {
        for (i = 0, x = 0; i < n; i++, x+=dx)
            a[i] = sin(M_PI*x);
    }
    else if (!strncmp(ic, "spikes(", 7)) /* spikes(Const,Amp,Loc,Amp,Loc,...) */
    {
        char *next;
        double cval = strtod(ic+7, &next);
        char const *p = next;
        for (i = 0, x = 0; i < n; i++)
            a[i] = cval;
        while (*p != ')')
        {
            char *ep_amp, *ep_idx;
            double amp = strtod(p+1, &ep_amp);
            int idx = (int) strtod(ep_amp+1, &ep_idx);
            assert(idx<n);
            a[idx] = amp;
            p = ep_idx;
        }

    }

    write_array(TSTART, Nx, dx, a);
}

static void 
compute_exact_solution(int n, Double *a, Double dx, char const *ic,
    Double alpha, Double t, Double bc0, Double bc1)
{
    int i;
    Double x;
    
    if (bc0 == 0 && bc1 == 0 && !strncmp(ic, "sin(Pi*x)", 9))
    {
        for (i = 0, x = 0; i < n; i++, x+=dx)
            a[i] = sin(M_PI*x)*exp(-alpha*M_PI*M_PI*t);
    }
    else if (bc0 == 0 && bc1 == 0 && !strncmp(ic, "const(", 6))
    {
        Double cval = strtod(ic+6, 0);
        for (i = 0, x = 0; i < n; i++, x+=dx)
        {
            int n;
            Double fsum = 0;

            /* sum first 200 terms of Fourier series */
            for (n = 1; n < 200; n++)
            {
                Double coeff = 2*cval*(1-pow(-1.0,(double)n))/(n*M_PI);
                Double func = sin(n*M_PI*x)*exp(-alpha.x*n*n*M_PI*M_PI*t.x);
                fsum += coeff * func;
            }
            a[i] = fsum;
        }
    }
    else /* can only compute final steady state solution */
    {
        for (i = 0, x = 0; i < n; i++, x+=dx)
            a[i] = bc0 + (bc1-bc0)*x;
    }
}

static void
solution_update_ftcs(int n, Double *curr, Double const *last,
    Double alpha, Double dx, Double dt,
    Double bc_0, Double bc_1)
{
    Double const r = alpha * dt / (dx * dx);

    /* Impose boundary conditions for solution indices i==0 and i==n-1 */
    curr[0  ] = bc_0;
    curr[n-1] = bc_1;

    /* Update the solution using FTCS algorithm */
    for (int i = 1; i < n-1; i++)
        curr[i] = r*last[i+1] + (1-2*r)*last[i] + r*last[i-1];
}

static void
solution_update_upwind15(int n, Double *curr, Double const *last,
    Double alpha, Double dx, Double dt,
    Double bc_0, Double bc_1)
{
    Double const f2 = 1.0/24;
    Double const f1 = 1.0/6;
    Double const f0 = 1.0/4;
    Double const k = alpha * alpha * dt / (dx * dx);
    Double const k2 = k*k;

    int i;
    curr[0  ] = bc_0;
    curr[1  ] = last[1  ] + k * (last[0  ] - 2 * last[1  ] + last[2  ]);
    curr[n-2] = last[n-2] + k * (last[n-3] - 2 * last[n-2] + last[n-1]);
    curr[n-1] = bc_1;
    for (i = 2; i < n-2; i++)
        curr[i] =  f2*(12*k2  -2*k    )*last[i-2]
                  +f2*(12*k2  -2*k    )*last[i+2]
                  -f1*(12*k2  -8*k    )*last[i-1]
                  -f1*(12*k2  -8*k    )*last[i+1]
                  +f0*(12*k2 -10*k  +4)*last[i  ];
}

static void 
r83_np_sl ( int n, Double const *a_lu, Double const *b, Double *x)
    /* Licensing: This code is distributed under the GNU LGPL license. 
       Modified: 30 May 2009 Author: John Burkardt
       Modified by Mark C. Miller, miller86@llnl.gov, July 23, 2017
    */
{
    int i;

    for ( i = 0; i < n; i++ )
        x[i] = b[i];

    /* Solve L * Y = B.  */
    for ( i = 1; i < n; i++ )
        x[i] = x[i] - a_lu[2+(i-1)*3] * x[i-1];

    /* Solve U * X = Y.  */
    for ( i = n; 1 <= i; i-- )
    {
        x[i-1] = x[i-1] / a_lu[1+(i-1)*3];
        if ( 1 < i )
            x[i-2] = x[i-2] - a_lu[0+(i-1)*3] * x[i-1];
    }
}

static void
solution_update_crankn(int n, Double *curr, Double const *last,
    Double alpha, Double dx, Double dt,
    Double bc_0, Double bc_1)
{
    /* Do the solve */
    r83_np_sl (n, cn_Amat, last, curr);
    curr[0] = bc0;
    curr[n-1] = bc1;
}

int finalize(int ti, Double maxt, Double change)
{
    int retval = 0;

    if (outi)
    {
        printf("Iteration %04d: last change l2=%g\n", ti, change.x);
        printf("Total adds = %d\n", Double::nadds);
        printf("Total mults = %d\n", Double::nmults);
        printf("Total divs = %d\n", Double::ndivs);
        printf("Total bytes = %lu\n", Double::nbytes);
    }

    delete [] curr;
    delete [] last;
    if (exact) delete [] exact;
    if (change_history) delete [] change_history;
    if (error_history) delete [] error_history;
    if (cn_Amat) delete [] cn_Amat;
    if (strncmp(alg, "ftcs", 4)) free((void*)alg);
    if (strncmp(prec, "double", 6)) free((void*)prec);
    if (strncmp(ic, "const(1)", 8)) free((void*)ic);

    return retval;
}

int main(int argc, char **argv)
{
    int i, ti;
    Double error;

    process_args(argc, argv);

    Double change;
    Nx = (int) (lenx/dx);
    Nt = (int) (maxt/dt);
    dx = lenx/(Nx-1);

    initialize();

    /* Initial condition */
    set_initial_condition(Nx, last, dx, ic);

    /* Iterate until residual is small or hit max iterations */
    for (ti = 0; ti*dt < maxt; ti++)
    {
        if (!strcmp(alg, "ftcs"))
            solution_update_ftcs(Nx, curr, last, alpha, dx, dt, bc0, bc1);
        else if (!strcmp(alg, "upwind15"))
            solution_update_upwind15(Nx, curr, last, alpha, dx, dt, bc0, bc1);
        else if (!strcmp(alg, "crankn"))
            solution_update_crankn(Nx, curr, last, alpha, dx, dt, bc0, bc1);

        if (ti>0 && save)
        {
            compute_exact_solution(Nx, exact, dx, ic, alpha, ti*dt, bc0, bc1);
            if (savi && ti%savi==0)
                write_array(ti, Nx, dx, exact);
        }

        if (ti>0 && savi && ti%savi==0)
            write_array(ti, Nx, dx, curr);

        change = l2_norm(Nx, curr, last);
        if (save)
        {
            change_history[ti] = change;
            error_history[ti] = l2_norm(Nx, curr, exact);
        }

        copy(Nx, last, curr);

        if (outi && ti%outi==0)
        {
            printf("Iteration %04d: last change l2=%g\n", ti, change.x);
        }
    }

    write_array(TFINAL, Nx, dx, curr);
    if (save)
    {
        write_array(RESIDUAL, ti, dt, change_history);
        write_array(ERROR, ti, dt, error_history);
    }

    return finalize(ti, maxt, change);
}
