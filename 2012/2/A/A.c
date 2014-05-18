#include <stdio.h>
#include <stdlib.h>
#define MAX_N 10000

long long d[MAX_N];

int cmp(const void * a, const void * b) {
	return d[*(long long *)a] - d[*(long long *)b];
}

int main() {
	long long T, N, l[MAX_N], D, t, i, j, m[MAX_N], v[MAX_N], a, b;
	
	scanf("%lld",&T);
	
	for (t = 1; t <= T; t++) {
		scanf("%lld",&N);
		for (i = 0; i < N; i++)
			scanf("%lld%lld",d+i,l+i);
		scanf("%lld",&D);
		
		for (i = 0; i < N; i++)
			v[i] = i;
		
		qsort(v, N, sizeof(long long), cmp);
		
		for (i = N-1; i >= 0; i--) {
			a = v[i];
			
			if (d[a] >= D)
				break;
			
			m[a] = (d[a]+l[a]>=D) ? (D-d[a]) : 0x7ffffffffffffff;
			
			for (j = i+1; j < N; j++) {
				b = v[j];
				
				if ( (d[b] > d[a] + l[a]) || (d[b] >= D) ) {
					break;
				}
				
				if (m[b] <= (d[b]-d[a])) {
					m[a] = d[b] - d[a];
					break;
				}
			}
		}
		
		printf("Case #%lld: %s\n",t, (m[0] <= d[0]) ? "YES" : "NO");
	}
	
	return 0;
}
