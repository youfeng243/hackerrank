#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

class HRML
{
public:
    
    HRML()
    {
    }
    
    HRML(string& tag, string _origin)
    {
        m_name = tag;
        m_origin = _origin;
        
        //cout<<m_origin<<endl;
        Parase();
        
        //printMap();
    }
    
    HRML(const HRML& c )
    {
        m_attribute = c.m_attribute;
        m_origin = c.m_origin;
        m_name = c.m_name;
        m_chirdArray = c.m_chirdArray;
    }
    
    void Parase()
    {
        int length = m_origin.length();
        int i = 0;
        int j = 0;
        int mark = 0;
        int findindex = 0;
        string tag = "";
        string temp = "";
        
        while( i < length )
        {
            if( m_origin[i] == '<' && m_origin[i + 1] != '/' )
            {
                mark = i;
                i++;
                tag = "";
                
                while( i < length )
                {
                    if( m_origin[i] == ' ' )
                    {
                        i++;
                        continue;
                    }
                    break;
                }
                
                while( i < length )
                {
                    if( m_origin[i] == ' ' )
                    {
                        break;
                    }
                    tag += m_origin[i];
                    i++;
                }
                
                tag = trim(tag, " ");
                if( tag == m_name )
                {
                    j = i;
                    temp = "";
                    int cnt = 0;
                    while ( j < length )
                    {
                        if( m_origin[j] == '\"' )
                        {
                            cnt++;
                        }
                        
                        if( m_origin[j] == '>' && cnt % 2 == 0 )
                        {
                            break;
                        }
                        temp += m_origin[j];
                        j++;
                    }
                    

                    ParaseValue( temp );
                    i = j;
                }
                else
                {
                    findindex = m_origin.find(tag, i);
                    if( findindex != string::npos )
                    {
                        while(findindex < length)
                        {
                            if(m_origin[findindex] == '>')
                            {
                                break;
                            }
                            findindex++;
                        }   
                        HRML hrml(tag, m_origin.substr(mark, findindex + 1 - mark));
                        
                        m_chirdArray[tag] = hrml;
                        i = findindex;
                    }
                }
            }
            i++;   
        }
    }
    
    
    void ParaseValue( string value )
    {
        int i = 0;
        int length = 0;
        string key = "";
        string val = "";
        
        value = trim(value, " ");
        //cout<<value<<endl;
        
        if( value.length() <= 0 )
        {
            return;
        }
        
        length = value.length();
        while( i < length )
        {
            key = "";
            while( i < length )
            {
                if( value[i] == '=' )
                {
                    break;
                }
                key += value[i];
                i++;
            }
            
            while( i < length )
            {
                if( value[i] != '\"' )
                {
                    i++;
                    continue;
                }
                break;
            }
            
            i++;
            val = "";
            while( i < length )
            {
                if( value[i] != '\"' )
                {
                    val += value[i];
                    i++;
                    continue;
                }
                break;
            }
            
            key = trim(key, " ");
            
            //cout<<key<<endl;
            //cout<<val<<endl;
            
            m_attribute[key] = val;
            i++;
        }
        
    }
    
    string Find( string text )
    {
        text = trim(text, " ");
        if( text[0] == '~' )
        {
            if( m_attribute.count(text.substr(1)) > 0 )
            {
                return m_attribute[text.substr(1)];
            }
            else
            {
                return "Not Found!";
            }
        }
        
        return ParaFind(text.substr(1));
    }
    
    string ParaFind( string text )
    {
        int i = 0;
        int length = text.length();
        string tag = "";
        
        while( i < length )
        {
            if( text[i] != '.' && text[i] != '~' )
            {
                tag += text[i];
                i++;
                continue;
            }
            break;
        }
        
        tag = trim(tag, " ");
        
        map< string, HRML >::iterator iter;
        for( iter = m_chirdArray.begin(); iter != m_chirdArray.end(); iter++ )
        {
            if( iter->first == tag )
            {
                return m_chirdArray[tag].Find(text.substr(i));
            }
        }
        
        return "Not Found!";
    } 
    
private:
    string& trim(string &s, string c)   
    {  
        if (s.empty())   
        {  
            return s;  
        }  
        s.erase(0,s.find_first_not_of(c));  
        s.erase(s.find_last_not_of(c) + 1);  
        return s;  
    }
    
    void printMap( void )
    {
        map<string, string>::iterator iter;
        for( iter = m_attribute.begin(); iter != m_attribute.end(); iter++ )
        {
            cout<<iter->first<<" " << iter->second<<endl;
        }
    }
        
private:
    map<string, string> m_attribute;

    string m_origin;
    
    string m_name;
    
    map<string, HRML> m_chirdArray;
};

string& Trim(string &s, string c)   
{  
    if (s.empty())   
    {  
        return s;  
    }  
    s.erase(0,s.find_first_not_of(c));  
    s.erase(s.find_last_not_of(c) + 1);  
    return s;  
}

void Parase(map< string, HRML > &all, string origin)
{
    int i = 0;
    int mark = 0;
    int findindex = 0;
    int length = origin.length();
    
    while (i < length)
    {
        string tag = "";
        if( origin[i] == '<' && origin[i + 1] != '/' )
        {
            mark = i;
            i++;
            
            while( i < length )
            {
                if( origin[i] == ' ' )
                {
                    i++;
                    continue;
                }
                break;
            }
            
            while( i < length )
            {
                if(origin[i] == ' ')
                {
                    break;
                }
                tag += origin[i];
                i++;
            }
            findindex = origin.find(tag, i);
            if( findindex != string::npos )
            {
                while(findindex < length)
                {
                    if(origin[findindex] == '>')
                    {
                        break;
                    }
                    findindex++;
                }   
                HRML hrml(tag, origin.substr(mark, findindex + 1 - mark));
                all[tag] = hrml;
                i = findindex;
            }
        }
        i++;
    }    
}

void Find( string text, map< string, HRML >& all )
{
    int i = 0;
    int length = text.length();
    string tag = "";
    
    while( i < length )
    {
        if( text[i] != '.' && text[i] != '~' )
        {
            tag += text[i];
            i++;
            continue;
        }
        break;
    }
    
    tag = Trim(tag, " ");
    
    bool findFlag = false;
    map< string, HRML >::iterator iter;
    for( iter = all.begin(); iter != all.end(); iter++ )
    {
        if( iter->first == tag )
        {
            cout<<all[tag].Find(text.substr(i))<<endl;
            findFlag = true;
            break;
        }
    }
    
    if( findFlag == false )
    {
        cout<<"Not Found!"<<endl;
    }
    
}

int main() 
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int N = 0;
    int Q = 0;
    string origin = "";
    string temp = "";
    map< string, HRML > all;
    
    cin>>N>>Q;
    cin.get();
    for( int i = 0; i < N; i++ )
    {
        getline(cin, temp);
        origin += temp;
    }
    
    Parase(all, origin);
    
    for( int i = 0; i < Q; i++ )
    {
        cin>>temp;
        Find(temp, all);
    }
    
    return 0;
}
