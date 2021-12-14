#include<iostream>

using namespace std;

int main(){
	//kill the marco Mate WM
	system("killall marco");
	system("killall caja");
	//launch the custom daemons
	system("/data/data/com.termux/files/usr/lib/xfce4/notifyd/xfce4-notifyd &");
	system("xfdesktop &");
	system("xfwm4 &");
	system("export QT_QPA_PLATFORMTHEME=qt5ct");
	return 0;
	}
