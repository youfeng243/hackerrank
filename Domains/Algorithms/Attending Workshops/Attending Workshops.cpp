#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool cmp( const pair<int, int> a, const pair<int, int> b)
{
    if( a.second == b.second )
    {
        return a.first < b.first;
    }
    
    return a.second < b.second;
}

class Available_Workshops
{
public:
    Available_Workshops( int *starttime, int *duration, int n )
    {
        cnt = 0;
        for( int i = 0; i < n; i++ )
        {
            pair<int, int> time(starttime[i], starttime[i] + duration[i]);
            m_array.push_back(time);
        }
        sort(m_array.begin(), m_array.end(), cmp);
        
        cnt = 1;
        int prestart = m_array[0].first;
        int preend = m_array[0].second;
        for( int i = 1; i < n; i++ )
        {
            if( m_array[i].first >= preend )
            {
                prestart = m_array[i].first;
                preend = m_array[i].second;
                cnt++;
            }
        }
    }
    
    int getAnswer()
    {
        return cnt;
    }
    
    
private:
    int cnt;
    vector< pair<int, int> > m_array;
};

int CalculateMaxWorkshops( Available_Workshops *ptr )
{
    return ptr->getAnswer();
}

Available_Workshops *initialize( int *starttime, int *duration, int n )
{
    Available_Workshops *ptr = new Available_Workshops(starttime, duration, n);
    
    return ptr;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int n;
    cin>>n;
    int start_time[n],duration[n];
    for(int i=0;i<n;i++)
    {
        cin>>start_time[i];
    }
    for(int i=0;i<n;i++)
    {
        cin>>duration[i];
    }
    
    Available_Workshops * ptr;
    ptr=initialize(start_time,duration,n);
    cout<<CalculateMaxWorkshops(ptr)<<endl;
    return 0;
}
