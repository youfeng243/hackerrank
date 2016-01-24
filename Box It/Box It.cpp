#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int BoxesCreated,BoxesDestroyed;

class Box
{
public:
    Box()
    {
        length = 0;
        breadth = 0;
        height = 0;
        BoxesCreated++;
    }
    Box(int l, int b, int h)
    {
        length = l;
        breadth = b;
        height = h;
        BoxesCreated++;
    }
    
    Box(const Box &b)
    {
        length = b.length;
        breadth = b.breadth;
        height = b.height;
        BoxesCreated++;
    }
    
    int getLength()
    {
        return length;
    }
    
    int getBreadth()
    {
        return breadth;
    }
    
    int getHeight()
    {
        return height;
    }
    
    long long CalculateVolume()
    {
        return (long long)length * (long long)breadth * (long long)height;
    }
    
    ~Box()
    {
        BoxesDestroyed++;
    }
    
    bool operator<( const Box &c )
    {
        if( breadth == c.breadth && length == c.length )
        {
            return height < c.height;
        }
        
        if( length == c.length )
        {
            return breadth < c.breadth; 
        }
        
        return length < c.length;
    }
    
    friend ostream &operator<<(ostream &os, const Box c);
    
private:
    int length;
    int breadth;
    int height;
};

ostream &operator<<(ostream &os, const Box c)
{
    os<<c.length << " " << c.breadth << " " << c.height;
    return os;
}


void check2()
{
    int n;
    cin>>n;
    Box temp;
    for(int i=0;i<n;i++)
    {
    int type;
    cin>>type;
    if(type ==1)
        {
            cout<<temp<<endl;
        }
        if(type == 2)
        {
            int l,b,h;
            cin>>l>>b>>h;
            Box NewBox(l,b,h);
            temp=NewBox;
            cout<<temp<<endl;
        }
        if(type==3)
        {
            int l,b,h;
            cin>>l>>b>>h;
            Box NewBox(l,b,h);
            if(NewBox<temp)
            {
                cout<<"Lesser"<<endl;
        }
            else
            {
                cout<<"Greater"<<endl;
            }
        }
        if(type==4)
        {
            cout<<temp.CalculateVolume()<<endl;
        }
        if(type==5)
        {
            Box NewBox(temp);
            cout<<NewBox<<endl;
        }
    }
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    BoxesCreated = 0;
    BoxesDestroyed = 0;
    check2();
    cout<<"Boxes Created : "<<BoxesCreated<<endl<<"Boxes Destroyed : "<<BoxesDestroyed<<endl;
}
