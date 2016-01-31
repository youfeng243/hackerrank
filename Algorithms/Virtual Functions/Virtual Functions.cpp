#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person
{
public:
    virtual void getdata(void) = 0;
    virtual void putdata(void) = 0;
protected:
    string name;
    int age;    
};


class Professor: public Person
{
public:
    Professor()
    {
        count++;
        curid = count;
    }
    
    void getdata(void)
    {
        cin>>name>>age>>publications;
    }
    
    void putdata(void)
    {
        cout<<name<<" "<<age<<" "<<publications<<" "<<curid<<endl;
    }
private:
    static int count;
    int publications;
    int curid;
};
int Professor::count = 0;



class Student: public Person
{
public:
    Student()
    {
        count++;
        curid = count;
    }
    void getdata(void)
    {
        int score = 0;
        
        cin>>name>>age;
        sum = 0;
        for( int i = 0; i < 6; i++ )
        {
            cin>>score;
            sum += score;
        }
    }
    
    void putdata(void)
    {
        cout<<name<<" "<<age<<" "<<sum<<" " <<curid<<endl;
    }
private:
    static int count;
    int sum;
    int curid;
};
int Student::count = 0;


int main(){

    freopen("in.txt","r",stdin);
    freopen("out.txt", "w", stdout);

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
