#ifndef MYSTRING_H
#define MYSTRING_H

#include <iostream>

class MyString {
private:
    char* str;  // dynamically allocated C-style string
    int len;    // length of the string

public:
    MyString();

    MyString(const char* s);

    MyString(const MyString& other);

    ~MyString();

    int length() const;

    const char* c_str() const;

    void append(const MyString& other);

    int compare(const MyString& other) const;

    MyString& operator=(const MyString& other);

    MyString operator+(const MyString& other) const;

    bool operator==(const MyString& other) const;

    friend std::ostream& operator<<(std::ostream& os, const MyString& s);

    MyString substring(int start, int end) const;
};

#endif
