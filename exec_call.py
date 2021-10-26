#import mainwindow as wm
from os import system

def style():
    system("lxappearance")

def wm_settings():
    system("xfwm4-settings")

def wm_tweaks_settings():
    system("xfwm4-tweaks-settings")

def workspace_settings():
    system("xfwm4-workspace-settings")
    
def df_apps_settings():
	system("xfce4-mime-settings")

def mate_ss_settings():
    system("mate-session-properties")


