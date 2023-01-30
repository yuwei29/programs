#include <stdio.h>
#include<chrono>
#include<iostream>
#include<fstream>
#define MAX_FILE_NAME 100

int main()
{
    using namespace std;
    using namespace std::chrono;
	char filename[MAX_FILE_NAME];
    char ofilename[MAX_FILE_NAME];
	char c; // To store a character read from file

	// Get file name from user. The file should be
	// either in current folder or complete path should be provided
	printf("Enter infile name: ");
	scanf("%s", filename);
    printf("Enter outfile name: ");
	scanf("%s", ofilename);

	// Open the file
    auto start = steady_clock::now();
	
	ifstream ifile(filename);
    ofstream ofile(ofilename);
	// Check if file exists
	if (!ifile.is_open())
	{
		printf("Could not open file %s", filename);
		return 0;
	}
	string line;
	// Extract characters from file and store in character c
	while(getline(ifile,line))
		ofile<<line<<"\n";

	// Close the file
	auto end = steady_clock::now();
	ifile.close();
    ofile.close();
	cout<<"import file using "<<duration_cast<seconds>(end-start).count()<<" seconds\n";

	return 0;
}
