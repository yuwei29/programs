/* C Program to count the Number of Lines in a Text File */
#include <stdio.h>
#include<chrono>
#include<iostream>
#include<fstream>
#define MAX_FILE_NAME 100

int main()
{
    using namespace std;
    using namespace std::chrono;
	//FILE *fp;
	int count = 0; // Line counter (result)
	char filename[MAX_FILE_NAME];
	char c; // To store a character read from file

	// Get file name from user. The file should be
	// either in current folder or complete path should be provided
	printf("Enter file name: ");
	scanf("%s", filename);

	// Open the file
    auto start = steady_clock::now();
	
	ifstream ifile(filename);
	// Check if file exists
	if (!ifile.is_open())
	{
		printf("Could not open file %s", filename);
		return 0;
	}
	string line;
	// Extract characters from file and store in character c
	while(getline(ifile,line))
		count++;

	// Close the file
	auto end = steady_clock::now();
	ifile.close();
	cout<<"count lines using "<<duration_cast<seconds>(end-start).count()<<" seconds\n";
	printf("The file %s has %d lines\n ", filename, count);

	return 0;
}
