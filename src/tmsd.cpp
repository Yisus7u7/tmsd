#include<iostream>

using namespace std;

int main(){
	//kill the marco Mate WM
	system("killall marco");
	//launch the custom daemons
	system("lxqt-notificationd &");
	system("xfdesktop &");
	system("xfwm4 &");
	system("export QT_QPA_PLATFORMTHEME=qt5ct");
	return 0;
	}
