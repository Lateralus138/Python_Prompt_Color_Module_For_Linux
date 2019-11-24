#!/usr/bin/env python3
def prompt_color(fg_color = '',bg_color = '',style = 0,clear = True):
    """Change prompt color

    @USAGE:\tprompt_color([30-37,90-97],[100-107],[0-5])
    
    @PARAM\t@DESCRIPTION
    fg_color\t[30-37,90-97] Foreground Color
    bg_color\t[100-107] Background Color
    style\t[0-5] None,Normal,Bold
    \t\t,Dark,Italic,Blink
    clear\tClear the screen to make settings active
    \t\tTrue|False"""
    from subprocess import call
    strInit,strBody,strEnd = '\e[','','m'
    if (fg_color not in range(30, 38) and
            fg_color not in range(90, 98) and
            fg_color != 0):
                fg_color = 0
    if (bg_color not in range(100, 108) and
            bg_color != 0):
                bg_color = ''
    if (style not in range(0, 6)):
                style = 0
    strBody = strBody + str(style) + ';'
    strBody = strBody + str(fg_color)
    if bg_color:
        strBody = strBody + ';' + str(bg_color)
    body = strInit + strBody + strEnd
    call('printf ' + "''" + '"' + body + '"' + (';clear' if clear else ''),shell=True) 

def cd(path=''):
    '''Change Directory for Python
    
    @USAGE:\tcd(<PATH>)'''
    import os
    if path == '':
        path = os.environ['HOME']
    if os.path.isdir(path):
        try:
            os.chdir(path)
        except:
            print('Permission denied.')
    else:
    	print('{} does not exist.'.format(path))

def clear():
    '''Clear screen Python Linux

    @USAGE\tclear()'''
    import os
    os.system('clear')

