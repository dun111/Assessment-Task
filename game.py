"""
TalesOfTime: A text-based adventure game where you defeat 5 bosses
and 3 secret bosses to save Fargon (Main part)
"""
# GameName TalesOfTime
# StudentName EricZheng
# GameDuration: This game should go for around an hour on average.
# Uses Upper_Case naming style for constants and snake_case for functions and variables
# Imports
import time
import json
import random

# Global variables to be used throughout the game
PLAYER = None
USERNAME = ""
COMPANION = ""
CURRENT_CHAPTER = "main"

# Ascii art saved as a list
BULL = r"""
      
             _.-````'-,_
   _,.,_ ,-'`           `'-.,_
 /)     (\                   '``-.
((      ) )                      `\
 \)    (_/                        )\
  |       /)           '    ,'    / \
  `\    ^'            '     (    /  ))
    |      _/\ ,     /    ,,`\   (  "`
     \Y,   |  \  \  | ````| / \_ \
       `)_/    \  \  )    ( >  ( >
                \( \(     |/   |/
               /_(/_(    /_(  /_( 
      
"""
# Saves ascii as a raw string and use ''' for the art. Repeats for the rest
FLAME = r"""
         
                  __~a~_
                  ~~;  ~_
    _                ~  ~_                _
   '_\;__._._._._._._]   ~_._._._._._.__;/_`
   '(/'/'/'/'|'|'|'| (    )|'|'|'|'\'\'\'\)'
   (/ / / /, | | | |(/    \) | | | ,\ \ \ \)
  (/ / / / / | | | ^(/    \) ^ | | \ \ \ \ \)
 (/ / / / /  ^ ^ ^   (/  \)    ^ ^  \ \ \ \ \)
(/ / / / ^          / (||)|          ^ \ \ \ \)
^ / / ^            M  /||\M             ^ \ \ ^
 ^ ^                  /||\                 ^ ^
                     //||\\
                     //||\\
                     //||\\         
                     '/||\'

"""

GOLEM = r"""
         
⠀⠀⠀⠀⠀⠀⢀⡀⣴⡄⢸⣀⣀⣈⣿⣿⣁⣀⣀⡇⢠⣦⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠴⠾⠿⠿⠛⠃⠀⠛⠛⠛⠛⠛⠛⠛⠛⠀⠘⠛⠿⠿⠷⠦⠀⠀⠀⠀
⠀⠀⢀⣤⣤⣴⡆⢀⣶⣾⣿⣿⣷⣦⡀⢀⣴⣾⣿⣿⣷⣶⡀⢰⣦⣤⣤⡀⠀⠀
⠀⢠⣾⣿⣿⣿⠇⢸⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⡇⠸⣿⣿⣿⣷⡄⠀
⠀⠈⠛⣿⣿⣿⠀⠀⡉⠛⠿⠛⢉⣿⡇⢸⣿⡉⠛⠿⠛⢉⠀⠀⣿⣿⣿⣿⠁⠀
⠀⠀⣾⣿⣿⣿⠀⠀⢿⣷⣶⣿⣿⣿⡇⢸⣿⣿⣿⣄⣼⡿⠀⠀⣿⣿⣿⣿⠀⠀
⠀⠀⠘⢉⣉⣉⠀⠀⠸⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⠇⠀⠀⣉⣉⡉⠁⠀⠀
⠀⠀⠈⣿⣿⣿⡀⠀⠀⣄⣈⠉⠉⠙⠃⠘⠋⣉⣉⣁⣠⠀⠀⢀⣿⣿⣿⠀⠀⠀
⠀⠀⠀⢹⣿⣿⡇⠀⢠⣿⣿⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⢸⣿⣿⡏⠀⠀⠀
⠀⠀⠀⠘⣿⣿⣇⠀⢸⣿⣿⣿⣿⣿⠏⠹⣿⣿⣿⣿⣿⡇⠀⣸⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠛⠛⠋⠀⣸⣿⣿⣿⣿⠏⠀⠀⠹⣿⣿⡿⣿⣇⠀⠙⠃⠈⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⠉⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀

"""


WRAITH = r"""
          
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⢠⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠄⠀⠀⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠀⠀⠀⠀⣸⣦⣸⣧⣼⣿⣦⣄⣀⣈⣴⣾⣿⣿⣦⡐⠄⠀⠀⠀⠀
⠀⢠⣶⣶⣦⣤⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡌⡀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢠⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠄⢿⣿⣿⣿⡿⠿⣿⡿⠉⠙⣿⣿⣿⣿⣿⣿⡇⢘⠐⠨⠄⠁⠄⢻⣿⣿⠀⠀⠀
⠀⠀⡈⢿⣿⣿⡇⠆⠈⠃⠃⠁⠸⣿⣿⣿⣿⣿⣷⢸⠀⠀⠀⠀⠈⡈⢿⡿⢀⠀⠀
⠀⠀⠀⠄⠻⣿⣇⠠⠀⠀⠀⠀⠂⢹⣿⣿⣿⣿⣿⠈⠀⠀⠀⠀⠀⢀⠸⠋⠄⠀⠀
⠀⠀⠀⠀⠀⠈⠻⡆⠀⠀⠀⠀⠈⠄⢿⣿⣿⣿⡆⠂⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠈⠄⢻⣿⣿⣧⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⠹⣿⣿⡀⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⢿⣿⡀⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⡙⠳⠈⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

DESBIO = r"""

  .:'                                  `:.
 ::'                                    `::
:: :.                                  .: ::
 `:. `:.             .             .:'  .:'
   `::. `::          !           ::' .::'
      `::.`::.    .' ! `.    .::'.::'
        `:.  `::::'':!:``::::'   ::'
        :'*:::.  .:' ! `:.  .:::*`:
       :: HHH::.   ` ! '   .::HHH ::
      ::: `H TH::.  `!'  .::HT H' :::
      ::..  `THHH:`:   :':HHHT'  ..::
      `::      `T: `. .' :T'      ::'
        `:. .   :         :   . .:'
          `::'               `::'
            :'  .`.  .  .'.  `:
            :' ::.       .:: `:
            :' `:::     :::' `:
             `.  ``     ''  .'
              :`...........':
              ` :`.     .': '
               `:  `...'  :' 

"""

MYSTERIOUS_CHARACTER = r"""
                                    
           *************
          *****     *****
         ***           ***
        ***             ***
        **               **
        **    o     o    **                  ____
        ***             ***             //////////
        ****           ****        ///////////////  
        *****         *****    ///////////////////
        ******       ******/////////         |  |
      *********     ****//////               |  |
   *************   **/////*****              |  |
  *************** **///***********          *|  |*
 ************************************    ****| <=>*
*********************************************|<===>* 
*********************************************| <==>*
***************************** ***************| <=>*
******************************* *************|  |*
********************************** **********|  |*    
*********************************** *********|  | 
                         """


NECRON_SECOND_FORM = r"""
                      <>=======() 
(/\___   /|\\          ()==========<>_
      \_/ | \\        //|\   ______/ \)
        \_|  \\      // | \_/
          \|\/|\_   //  /\/
           (oo)\ \_//  /
          //_/\_\/ /  |
         @@/  |=\  \  |
              \_=\_ \ |
                \==\ \|\_ 
             __(\===\(  )\
            (((~) __(_/   |
                 (((~) \  /
                 ______/ /
                 '------' """

NECRON = r"""
                           \ __
--==/////////////[})))==*
                 / \ '          ,|
                    `\`\      //|                             ,|
                      \ `\  //,/'                           -~ |
   )             _-~~~\  |/ / |'|                       _-~  / ,
  ((            /' )   | \ / /'/                    _-~   _/_-~|
 (((            ;  /`  ' )/ /''                 _ -~     _-~ ,/'
 ) ))           `~~\   `\\/'/|'           __--~~__--\ _-~  _/, 
((( ))            / ~~    \ /~      __--~~  --~~  __/~  _-~ /
 ((\~\           |    )   | '      /        __--~~  \-~~ _-~
    `\(\    __--(   _/    |'\     /     --~~   __--~' _-~ ~|
     (  ((~~   __-~        \~\   /     ___---~~  ~~\~~__--~ 
      ~~\~~~~~~   `\-~      \~\ /           __--~~~'~~/
                   ;\ __.-~  ~-/      ~~~~~__\__---~~ _..--._
                   ;;;;;;;;'  /      ---~~~/_.-----.-~  _.._ ~\     
                  ;;;;;;;'   /      ----~~/         `\,~    `\ \        
                  ;;;;'     (      ---~~/         `:::|       `\\.      
                  |'  _      `----~~~~'      /      `:|        ()))),      
            ______/\/~    |                 /        /         (((((())  
          /~;;.____/;;'  /          ___.---(   `;;;/             )))'`))
         / //  _;______;'------~~~~~    |;;/\    /                ((   ( 
        //  \ \                        /  |  \;;,\                 `   
       (<_    \ \                    /',/-----'  _> 
        \_|     \\_                 //~;~~~~~~~~~ 
                 \_|               (,~~   
                                    \~\
                                     ~~ """

CREDIT_ROLL = r"""
                     .''.      .        *''*    :_\/_:     .
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :    /)\   ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::.  | ' *''*    * '.\'/.'_\(/_'.':'.'
 : /\ : :::::  =  *_\/_*     -= o =- /)\    '  *
  '..'  ':::' === * /\ *     .'/.\'.  ' ._____
"""

DUNGEON_1 = r"""

               )\         O_._._._A_._._._O         /(
                \`--.___,'=================`.___,--'/
                 \`--._.__                 __._,--'/
                   \  ,. l`~~~~~~~~~~~~~~~'l ,.  /
       __            \||(_)!_!_!_.-._!_!_!(_)||/            __
       \\`-.__        ||_|____!!_|;|_!!____|_||        __,-'//
        \\    `==---='-----------'='-----------`=---=='    //
        | `--.                                         ,--' |
         \  ,.`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',.  /
           \||  ____,-------._,-------._,-------.____  ||/
            ||\|___!`======="!`======="!`======="!___|/||
            || |---||--------||-| | |-!!--------||---| ||
  __O_____O_ll_lO_____O_____O|| |'|'| ||O_____O_____Ol_ll_O_____O__
  o H o o H o o H o o H o o |-----------| o o H o o H o o H o o H o
 ___H_____H_____H_____H____O =========== O____H_____H_____H_____H___
                          /|=============|\
()______()______()______() '==== +-+ ====' ()______()______()______()
||{_}{_}||{_}{_}||{_}{_}/| ===== |_| ===== |\{_}{_}||{_}{_}||{_}{_}||
||      ||      ||     / |====  (   )  ====| \     ||      ||      ||
======================()  =================  ()======================
----------------------/| ------------------- |\----------------------
                     / |---------------------| \
-'--'--'           ()  '---------------------'  ()
                   /| ------------------------- |\    --'--'--'
       --'--'     / |---------------------------| \    '--'
                ()  |___________________________|  ()           '--'-
  --'-          /| _______________________________  |\
 --'          / |__________________________________| \ """

DUNGEON_2 = r"""
                                /   \              /'\       _                              
*\_..           /'.,/     \_         .,'   \     / \_                            
*    \         /            \      _/       \_  /    \     _                     
*     \__,.   /              \    /           \/.,   _|  _/ \                    
*          \_/                \  /',.,''\      \_ \_/  \/    \                   
*                           _  \/   /    ',../',.\    _/      \                  
*             /           _/m\  \  /    |         \  /.,/'\   _\                 
*           _/           /MMmm\  \_     |          \/      \_/  \                
*          /      \     |MMMMmm|   \__   \          \_       \   \_              
*                  \   /MMMMMMm|      \   \           \       \    \             
*                   \  |MMMMMMmm\      \___            \_      \_   \            
*                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          
*                    /'.,___________...,,'   \            \   \        \         
*                   /       \          |      \    |__     \   \_       \        
*                 _/        |           \      \_     \     \    \       \_      
*                /                               \     \     \_   \        \     
*                                                 \     \      \   \__      \    
*                                                  \     \_     \     \      \   
*                                                   |      \     \     \      \  
*                                                    \          |            \"    """


GOBLIN_HUT = r"""
                              ,-_                  (`  ).
                 |-_'-,              (     ).
                 |-_'-'           _(        '`.
        _        |-_'/        .=(`(      .     )
       /;-,_     |-_'        (     (.__.:-`-_.'
      /-.-;,-,___|'          `(       ) )
     /;-;-;-;_;_/|\_ _ _ _ _   ` __.:'   )
        x_( __`|_P_|`-;-;-;,|        `--'
        |\ \    _||   `-;-;-'
        | \`   -_|.      '-'
        | /   /-_| `
        |/   ,'-_|  \
        /____|'-_|___\
 _..,____]__|_\-_'|_[___,.._
'                          ``'--,..,.    """
SMALL_VILLAGE = r"""
                 ~         ~~          __
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/
'  |[]|,.--'' '',   ''-,.    |
  ..    ..-''    ;       ''. ' """
# Using upper case naming style for constants
DUNGEON_3 = r"""
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⣄⠙⠛⠛⠿⠿⠿⠟⢁⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⠘⠛⠿⢿⣿⠿⠻⣿⣿⣿⣿⣶⣶⣶⣦⣴⣿⣷⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣷⣶⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀
⠀⠀⠀⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢋⣀⠈⢿⣿⡟⢻⣿⣿⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣠⣤⣼⣿⣿⠀
⠀⠀⠀⢀⣠⣤⠈⠿⠿⠟⢋⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠐⣿⣿⣿⣷⣶⣤⣶⣿⣿⣿⣿⣿⣿⠟⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠐⣿⣿⣿⣷⣶⣤⣶⣿⣿⣿⣿⣿⣿⠟⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠐⣿⣿⣿⣷⣶⣤⣶⣿⣿⣿⣿⣿⣿⠟⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠐⣿⣿⣿⣷⣶⣤⣶⣿⣿⣿⣿⣿⣿⠟⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠙⠻⠿⠿⠿⣿⡿⣿⣿⣿⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⠛⠀⠀⠀⠀⠀⠀⢤⣶⣦⣀⣤⣿⣿⣿⠀
⠀⣠⣾⣿⡿⠿⠿⠿⠛⠋⠙⠋⠀⠸⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⠀
⠀⣿⣿⣿⣿⣶⣶⣶⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⢋⣡⠀
⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠛⠛⠛⠛⠀ """

DUNGEON_4 = r"""
               .                  .-.    .  _   *     _   .
           *          /   \     ((       _/ \       *    .
         _    .   .--'\/\_ \     `      /    \  *    ___
     *  / \_    _/ ^      \/\'__        /\/\  /\  __/   \ *
       /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .
  .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _
     /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \
   /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \
  /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.
@/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \%
@&8jgs@@%% @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)%
@88:::&(&8&&8:::::%&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8::::
`::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8:::::'
 `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.' """

DUNGEON_5 =  r"""
                             .          .           .     .                .       .
  .      .      *           .       .          .                       .
                 .       .   . *            
         >>         .        .               .
 .   .  /WWWI; \  .       .    .  ____               .         .     .         
  *    /WWWWII; \=====;    .     /WI; \   *    .        /\_             .
  .   /WWWWWII;..      \_  . ___/WI;:. \     .        _/M; \    .   .         .
     /WWWWWIIIIi;..      \__/WWWIIII:.. \____ .   .  /MMI:  \   * .
 . _/WWWWWIIIi;;;:...:   ;\WWWWWWIIIII;.     \     /MMWII;   \    .  .     .
  /WWWWWIWIiii;;;.:.. :   ;\WWWWWIII;;;::     \___/MMWIIII;   \              .
 /WWWWWIIIIiii;;::.... :   ;|WWWWWWII;;::.:      :;IMWIIIII;:   \___     *
/WWWWWWWWWIIIIIWIIii;;::;..;\WWWWWWIII;;;:::...    ;IMIII;;     ::  \     .
WWWWWWWWWIIIIIIIIIii;;::.;..;\WWWWWWWWIIIII;;..  :;IMIII;:::     :    \   
WWWWWWWWWWWWWIIIIIIii;;::..;..;\WWWWWWWWIIII;::; :::::::::.....::       \
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXXXXXXXXXXX """

TROLL = r"""
       .-'.'.'.'.'.'.`-.
     .'.'.'.'.'.'.'.'.'.`.
    /.'.'               '.\
    |.'    _.--...--._     |
    \    `._.-.....-._.'   /
    |     _..- .-. -.._   |
 .-.'    `.   ((@))  .'   '.-.
( ^ \      `--.   .-'     / ^ )
 \  /         .   .       \  /
 /          .'     '.  .-    \
( _.\    \ (_`-._.-'_)    /._\)
 `-' \   ' .--.          / `-'
     |  / /|_| `-._.'\   |
     |   |       |_| |   /-.._
 _..-\   `.--.______.'  |
      \       .....     |
       `.  .'      `.  /
         \           .'
           `-..___..-` """

SKELETON = r"""
                              _.--""-._
  .                         ."         ".
 / \    ,^.         /(     Y             |      )\
/   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
|        :|    `>   '.     l_..-------.._l      .'
|      __l;__ .'      "-.__.||_.-'v'-._||`"----"
 \  .-' | |  `              l._       _.'
  \/    | |                   l`^^'^^'j
        | |                _   \_____/     _
        j |               l `--__)-'(__.--' |
        | |               | /`---``-----'"1 |  ,-----.
        | |               )/  `--' '---'   \'-'  ___  `-.
        | |              //  `-'  '`----'  /  ,-'   I`.  \
      _ L |_            //  `-.-.'`-----' /  /  |   |  `. \
     '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
      `._;/7(-.......'  /        ) (     |  |            | |
      `._;l _'--------_/        )-'/     :  |___.    _._./ ;
        | |                 .__ )-'\  __  \  \  I   1   / /
        `-'                /   `-\-(-'   \ \  `.|   | ,' /
                           \__  `-'    __/  `-. `---'',-'
                              )-._.-- (        `-----'
                             )(  l\ o ('..-.
                       _..--' _'-' '--'.-. |
                __,,-'' _,,-''            \ \
               f'. _,,-'                   \ \
              ()--  |                       \ \
                \.  |                       /  \
                  \ \                      |._  |
                   \ \                     |  ()|
                    \ \                     \  /
                     ) `-.                   | |
                    // .__)                  | |
                 _.//7'                      | |
               '---'                         j_| `
                                            (| |
                                             |  \
                                             |lllj
                                             |||||  """

CHEST = r"""
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
  %%%%                """

CAPITAL = r"""
                      / \\\
                      |n| |
                    )(|_|-'X
                   /  \\Y// \
                   |A | | |A|
                   |  | | |_|
            )(__X,,|__|MEB;;;-,)(,
           /  \\\;;;;;;;;;;;;/    \
           |A | |            | U  |
         )_|  | |____)-----( |    |
        ///|__|-'////       \|___)=(__X
       /////////////         \///   \/ \
       |           |  U    U |//     \u|
       |   )_,-,___|_)=(     | |  U  |_|_X
       |  ///   \\|//   \    | |  __ |/// \
     )_')(//     \Y/     >---)=( /  \|  | |-----------------
    //// ,\ u   u |   u /////   \|  ||__|A|----------------
   |  | .. |      |    ///// ,-, \__||--------------------
---'--'_::_|______'----| u | | | |-----------------------.
                       |___|_|_|_|----------------------
                            `--------------------------
                                                                   """

ABANDONED_VILLAGE = r"""
                              /\  //\\
                       /\    //\\///\\\        /\
                      //\\  ///\////\\\\  /\  //\\
         /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \
        / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \. 
       /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       *
      /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\
     / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\
    / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\
   /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\
  /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\       |
 / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |           |
/ ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo  |
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo """

SPECIAL_SWORD = r"""
                             _
 _         | |
| | _______| |---------------------------------------------\
|:-)_______|==[]============================================>
|_|        | |---------------------------------------------/
           |_| """

SPECIAL_SHIELD = r"""
  |`-._/\_.-`|
  |    ||    |
  |___o()o___|
  |__((<>))__|
  \   o\/o   /
   \   ||   /
    \  ||  /
     '.||.'
       ``"""

SPECIAL_DAGGER = r"""
      ______________________________ ______________________
    .'                              | (_)     (_)    (_)   \
  .'                                |  __________________   }
.'_.............................____|_(                  )_/

"""

DARK_DAGGER = r"""                                   |_  |
                                                        | |
__                      ____                            | |
\ ````''''----....____.'\   ````''''--------------------| |--.               _____      .-.
 :.                      `-._                           | |   `''-----''''```     ``''|`: :|
  '::.                       `'--.._____________________| |                           | : :|
    '::..       ----....._______________________________| |                           | : :|
      `'-::...__________________________________________| |   .-''-..-'`-..-'`-..-''-.cjr :|
           ```'''---------------------------------------| |--'                         `'-'
                                                        | |
                                                       _| |
                                                      |___| """

DARK_BOOK = r"""
     __...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\ 
   //                 |                 \\ 
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================
                    `---`. """

DARK_SHIELD = r"""
  |\ _..--.._ /|
  |############|
   )##########(
._/##.'//\\'.##\_.
 .__)#((()))#(__.
  \##'.\\//.'##/
   \####\/####/
   /,.######.,\
  (  \##__##/  )
      "(\/)"
        )(.  """

DARK_SWORD = r"""               __________                         ._
             ./' .v~__,/~ _____   _____     _____   )~\      _____     _____
           ./  .(W---\| /',---.`\ |\./\     |\./|  / | \     |\./\     |\./|
          ,|  /@)$$$$$$$$($( )#H>===========) ) )==`\`\`\| | |=====\ \ \======`\`\`\| | |-->
/_p~~~~~~~~~~\$@|/------------/ / /-----`\`\\ | |------\ \ \-------`\`\\ | |-'
          `|  \) 
"""

SERPUS = r"""
                           .......................:....                                                       
              ..-=%--=---=-:..*...=*=......... .                                                    
             ..:*****+##%%%:*+==@..-*+*.#....-......                                                
            ....+#+%@+**#*%#%%#%+*.     %###=-++*+*=-...                                                
            ......*###+%%@#%%@%#=#*#*++###*#***@=+-...                                              
                ...=.*=##++##@#@%@%@%#@#@*##%###*%+. .                                              
                ....:..=**#%%###**%%#%%%@%%*%#+#%#%%=.                                              
                    .....+%%%%%*#==*#%@%@@%%@@@@%%%#%%..                                            
                    .....=#%%@@%=-=-#@@%#@@%%%@@@@@%##..                                            
                     ...-+#%+*+#+-%*%@#%*##*##*#%%%#%%#.                                            
                    ....-*##++*-**%%@*+....===++##%%%#%...                                          
                .......*#==+#=**%@#+....    ::****%%##@#.. .                                        
                ....-=%+=%#++%#%#+:.....    .-:=+##@%#@%.. .                                        
                ...*::%--**%%#..           .--=+*+###%@#=..                                         
                .:..--=+%%. ....           .:-=*=#%%%%@*.. .                                        
                ......... ......        ..:-=+#*#*%%@%%#....                                        
                      ..              ..-=-.*-+#%%%#%@%.=...                                        
                                    ..-:-:=+****@##%@%=.:...                                        
                                  ..=-.++**+=+%###%#%-..                                            
                                ..=-=.*-=+**#+%%%@@%.:..                                            
                              ..-::--+=.+*##@%#@@@@...                                              
                            ..:=-:+-+*+#*##%%@@@@%..                                                
                        ...:-:.--==+**#@#@%%%@@%:. .                                                
                        ..---=++*++*#*#%@@@%@%%==.....                                              
                ....  ..=.:-=+#=+++*#%#@@@@@%*#*##*.....                                            
                ..... :-:.=+*#+=++%##@%%%@%@@@%%%*%%-...                                            
            .....:+#=:..:=-=-+%%%@%@@@@@@@%%%%%#@%@@%. .        ..      ....                        
        .....-+**#%+----:+:=+*%#%%%@@@@@@@%%%%##%@@@@#..........:...........                        
        ..=*#%*##@%:=--+=*++%#%#@%@@@@@@@%@@#%@%@@%%@@.+##*#%*#*#***@*#*=*....                      
      ..+#**#%**%@::-:-==*###%@@%@@#@@@@%%#@%%@@%@%@@@@%%%%#@%@%##@#@##**+#%#...                    
    ...**#%#%%%@@%::==:*+**%%#@%%%@@@@@@%%%%%%#@@@@@@@@#%%%@@*@*%@@@%@@%@%@%%@#.                    
    ..=*%#%%#%*%%:--++++*#*@%##%@@%@@@%%%%@%@@@%@@@@@@@%%@@%@@%%@%%%###%#@%@@%@@-.......            
    .=#%@##%@#@@#-:=--=#*#*#%%@@@@@%@@@@@@@@@%%@@@@@@@@@@%@@@@@%%@%#%##@%%@@%%@@@%#+....            
    .+#%%@@#%@%%%=-=-=*#*%*@%@%%@@#%%@%@%@@@@@@@@@@@@@@@@@@%@@@*%@#%#%%@%%@@@@%@@@%#%#....          
    .++%#%@@%%@%%*-:--++*#+##@@@%%%@@@@@%@%@#@@%%%#%%%%%%@%#@*%@@@#%#%%%@@%%@%@%@@@%%#%% .          
    .=*%%@@%#%@%%#-=-*+++**#%#%@%#%@@%@@@@@#%#@@%%#%%#%%@%%%##@@%%#%@%@%%@%@@@@@@@@%%%#@@...        
    .*+*%@@@%%#@#@+=+=+*#%#**%%@@@%@%@@@@%%%@%@@@#@@%%@%%%@@*%@@#@#@@@%%%@%%@@@@@@@%#@@#%*..        
  ..:-*+**%%#%@%@@@++=*#=+######%@@@@%@%%%%%%@@#%%%@@%@@%%%@@%@%@%@%@%@@@@@@@@@@@@@@@*%@@@. ..      
...%+%%#####%##@@@%@*=-####%%%%%#%@@%@%%@%@@@@@@@%@%@#@@%@@@%@%%%@@%%@@@@@@@@@@@@@@%#@@%@@=... .    
..*##@+*%#%%%#%##%%%@=++*##%%%%%%%%%@%@@@@@@@%@@@@@@@%@@%@@@@@@@@@@@@@@@@@@@@@@@@@#%%@%@@@*#*...    
:-+##@@%#%@%%%#%%%%%@@@+#+***%%%%%%%%@@%@@@@@%@@@@@@@@%@%@@@@@@@@@@@@@@@@@@@@@@@%@%%@@@@@@#@*#:     
--==+@@#@@@@@@@@%%@%%@@@#%#*###%%%%%%%%%@@@@@@@@%@@@@@@%@%@%@@@@@@@@@@@@@@@@@%%@@@#%%@@@@@@@###.    
--==+#%@@@@@@@@@@@@@@@@@@@@%%%%##%%%#@@@%@%*##@@@@@@@@@%@@@@@@@@@@@@@@@@@%#%%#@#@@@%@@@@@@@@@%#:.   
:::--=++***###%%%@@@@@@@+*+#*%%%%%%%%*#@@#@#@@%@@@@@@@@@@@@@@@@@@@@@@%##%%%@%@%@@@@@@@@@%**=-:..    
.....::---==++++***####%+@#@@@@@@@%=#**#+%*%%%%@@@@@@@@@@@@%@%%%%@@%%%@@@@@@@@@@@@@@@@%#*++=-:..    
..........:::::----===+%@@+#@@%%%%%@*@@@%@@+#***@@@@@@%@@@%@@@@@@@@@@@@@@@@@@@@@@@%%#**++==-:...    
      ..................::....  ..                      
                                         ....... ....... ..                                    """

SAVE_FILE = "TalesOfTime.json"

def save_game():
    """
    Used to save game data to a json file
    """
    data = {
        "PLAYER": PLAYER,
        "USERNAME": USERNAME,
        "COMPANION": COMPANION,
        "CURRENT_CHAPTER": CURRENT_CHAPTER
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file)
    print("Waypoint set!")
#This saves the data (Name, PLAYER stats, COMPANION name and current chapter into a Json file

def load_game():
    """
    Used to extract data from the Json file and load the last saved chapter
    """
    global PLAYER, USERNAME, COMPANION, CURRENT_CHAPTER
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            PLAYER = data["PLAYER"]
            USERNAME = data["USERNAME"]
            COMPANION = data["COMPANION"]
            CURRENT_CHAPTER = data.get("CURRENT_CHAPTER", "main")
        print("Waypoint loaded!")
        # Resumes at the correct chapter
        resume_game()
    except FileNotFoundError:
        print("No saved waypoint found.")
        main()
        return
#This loads the json file data and if there is an error will show No saved waypoint

def resume_game():
    """
    Used to resume the game
    """
    if CURRENT_CHAPTER == "main":
        main()
    elif CURRENT_CHAPTER == "companion_chapter":
        companion_chapter()
    elif CURRENT_CHAPTER == "chapter_1":
        chapter_1()
    elif CURRENT_CHAPTER == "chapter_2":
        chapter_2()
    elif CURRENT_CHAPTER == "chapter_3":
        chapter_3()
    elif CURRENT_CHAPTER == "chapter_3part2":
        chapter_3part2()
    elif CURRENT_CHAPTER == "chapter_4":
        chapter_4()
    elif CURRENT_CHAPTER == "chapter_5":
        chapter_5()
    elif CURRENT_CHAPTER == "chapter_6":
        chapter_6()
    elif CURRENT_CHAPTER == "serpus_fight2":
        serpus_fight2()
    elif CURRENT_CHAPTER == "serpus_fight3":
        serpus_fight3()
    elif CURRENT_CHAPTER == "chapter_7":
        chapter_7()
    elif CURRENT_CHAPTER == "chapter_8":
        chapter_8()
    elif CURRENT_CHAPTER == "chapter_9":
        chapter_9()
    elif CURRENT_CHAPTER == "village":
        village()
    elif CURRENT_CHAPTER == "chapter_9part2":
        chapter_9part2()
    elif CURRENT_CHAPTER == "chapter_10":
        chapter_10()
    elif CURRENT_CHAPTER == "chapter_11":
        chapter_11()
    elif CURRENT_CHAPTER == "chapter_12":
        chapter_12()
    elif CURRENT_CHAPTER == "chapter_12part2":
        chapter_12part2()
    elif CURRENT_CHAPTER == "chapter_13":
        chapter_13()
    elif CURRENT_CHAPTER == "chapter_14":
        chapter_14()
    elif CURRENT_CHAPTER == "guardian1":
        guardian1()
    elif CURRENT_CHAPTER == "chapter_15":
        chapter_15()
    elif CURRENT_CHAPTER == "guardian2":
        guardian2()
    elif CURRENT_CHAPTER == "final_machine":
        final_machine()
    elif CURRENT_CHAPTER == "chapter_16":
        chapter_16()
    elif CURRENT_CHAPTER == "necron_fight":
        necron_fight()
    elif CURRENT_CHAPTER == "necron_fight2":
        necron_fight2()
    elif CURRENT_CHAPTER == "necron_fight3":
        necron_fight3()
    elif CURRENT_CHAPTER == "machines1":
        machines1()
    elif CURRENT_CHAPTER == "machines2":
        machines2()
    elif CURRENT_CHAPTER == "machines3":
        machines3()
    elif CURRENT_CHAPTER == "machines4":
        machines4()
    elif CURRENT_CHAPTER == "machines5":
        machines5()
    elif CURRENT_CHAPTER == "necron_fight4":
        necron_fight4()
    elif CURRENT_CHAPTER == "companion_fight":
        companion_fight()
    elif CURRENT_CHAPTER == "chapter_17":
        chapter_17()
    elif CURRENT_CHAPTER == "chapter_18":
        chapter_18()
    elif CURRENT_CHAPTER == "chapter_19":
        chapter_19()
    elif CURRENT_CHAPTER == "the_end":
        the_end()
    else:
        main()
# This function is used to go back to the PLAYER's
# chapter when the game saved by saving the current chapter into the variable "CURRENT_CHAPTER"

def decrease_health(amount=None):
    """
    Used to decrease the player's health
    If amount is not provided, it will randomly choose a value between 10 and 80.
    """
    if PLAYER is None:
        print("Error: PLAYER not initialized.")
        death()
        return
    if amount is None:
        amount = random.randint(10, 80)
    reduced = max(1, amount - PLAYER["defence"] // 3)
    PLAYER["health"] -= reduced
    print(f"You took {reduced} damage! (Reduced by defence) Your health is now {PLAYER['health']}.")
    if PLAYER["health"] <= 0:
        print("You have died...")
        death()
    elif PLAYER["health"] <= 10:
        print("Low Health!")
#This function lower's the PLAYER's health randomly between 10 and 80

def increase_health(amount):
    """
    Used to increase the player's health
    """
    if PLAYER is None:
        print("Error: PLAYER not initialized.")
        death()
        return
    PLAYER["health"] += amount
    print(f"Your health is now {PLAYER['health']}")
#This function increases the PLAYER's health

def reset_health():
    """
    Used to reset the player's health
    """
    if PLAYER is None:
        print("Error: PLAYER not initialized.")
        death()
        return
    PLAYER["health"] = 100
    print("Your health has been reset to 100.")
#This function resets the PLAYERs health

def playerdata(name):
    """
    The player's data for their stats by default
    """
    return {"name": name,
            "health": 100,
            "gold": 200,
            "strength": 20,
            "defence": 20,
            "luck": 20,}
#This function shows the PLAYER's stats. Still in work


def decrease_gold(amount):
    """
    Used to decrease the player's gold
    """
    if PLAYER is None:
        print("Error: PLAYER not initialized.")
        death()
        return
    PLAYER["gold"] -= amount
    print(f"You spent {amount} gold. Your gold is now {PLAYER['gold']}.")
#This function lowers the PLAYERs gold

def increase_gold(amount):
    """
    Used to increase the player's gold
    """
    if PLAYER is None:
        print("Error, PLAYER is not intitialized.")
        death()
        return
    PLAYER["gold"] += amount
    print(f"You gained {amount} gold. Your gold is now {PLAYER['gold']}")
#This function increases the PLAYER's gold

def death():
    """
    Used to kill the player then prompt them to restart or exit the game
    """
    print("You have died. Game over.")
    input()
    print("Do you want to restart the game? (Yes/No): ")
    choice = input().strip().strip().lower()
    if choice == "yes":
        restart()
    elif choice == "no":
        print("Thank you for playing!")
        exit()
    else:
        print("Bye! Exiting the game.")
        exit()
#This function manages the death sequence

def restart():
    """
    Used to restart the game and go to main
    """
    global USERNAME, COMPANION, PLAYER
    print("restarting the game...")
    USERNAME = ""
    PLAYER = None
    COMPANION = ""
    main()
#This function restarts the game

def dark_sword_story():
    """
    Used to upgrade sword and to show backstory
    """
    print("Before you leave, you notice a bottle of ominous energy.")
    input()
    print("Suddenly your sword flies out your hand and forges with the ominous energy")
    input()
    print("'You have acquired 'The Corrupted Sword'")
    input()
    print(DARK_SWORD)
    learn_more2 = input("Would you like to hear about the backstory of this weapon (Yes/No)?")
    match learn_more2.strip().lower().strip():
        case "yes":
            print("This sword, now corrupted by dark energy. " \
                  "Has increased sharpness and toughness allowing " \
                  "it attack against even the strongest of enemies.")
            input()
            chapter_10()
            return
        case "no":
            print("Ok, skipping backstory")
            input()
            chapter_10()
            return
        case _:
            print("Invalid Option")
            print("Try Again")
            dark_sword_story()
            return
#This is for the upgrade of the sword


def dark_shield_story():
    """
    Used to upgrade shield and to show backstory
    """
    print("Before you leave, you notice a bottle of ominous energy.")
    input()
    print("Suddenly your shield flies out your hand and forges with the ominous energy")
    input()
    print("'You have acquired 'The Dark Shield'")
    input()
    print(DARK_SHIELD)
    learn_more3 = input("Would you like to hear about the backstory of this weapon (Yes/No)?")
    match learn_more3.strip().lower().strip():
        case "yes":
            print("This shield, now corrupted by dark energy. " \
                  "Has increased defence and toughness allowing it defend " \
                  "against even the strongest of enemies.")
            input()
            chapter_12()
            return
        case "no":
            print("Ok, skipping backstory")
            input()
            chapter_12()
            return
        case _:
            print("Invalid Option")
            print("Try Again")
            dark_shield_story()
            return
#This is for the upgrade of the shield

def dark_dagger_story():
    """
    Used to upgrade dagger and to show backstory
    """
    print("Before you leave, you notice a bottle of ominous energy.")
    input()
    print("Suddenly your Dagger flies out your hand and forges with the ominous energy")
    input()
    print("'You have acquired 'The Dark Dagger'")
    input()
    print(DARK_SHIELD)
    learn_more3 = input("Would you like to hear about the backstory of this weapon (Yes/No)?")
    match learn_more3.strip().lower().strip():
        case "yes":
            print("This dagger, now corrupted by dark energy. " \
                  "Has increased sharpness and power allowing it attack " \
                  "against even the strongest of enemies.")
            input()
            chapter_7()
            return
        case "no":
            print("Ok, skipping backstory")
            input()
            chapter_7()
            return
        case _:
            print("Invalid Option")
            print("Try Again")
            dark_dagger_story()
            return
#This is for the upgrade of the shield

#Start of game with title screen
def main():
    """
    Main function to start the game and show the title screen
    """
    global USERNAME, PLAYER, CURRENT_CHAPTER
    CURRENT_CHAPTER = "main"
    print(r"""
 _________     _       _____     ________   ______      ___   ________ 
|  _   _  |   / \     |_   _|   |_   __  |.' ____ \   .'   `.|_   __  |
|_/ | | \_|  / _ \      | |       | |_ \_|| (___ \_| /  .-.  \ | |_ \_|
    | |     / ___ \     | |   _   |  _| _  _.____`.  | |   | | |  _|   
   _| |_  _/ /   \ \_  _| |__/ | _| |__/ || \____) | \  `-'  /_| |_    
 _|_____||____|_|____||________||________| \______.'  `.___.'|_____|   
|  _   _  ||_   _||_   \  /   _||_   __  |                             
|_/ | | \_|  | |    |   \/   |    | |_ \_|                             
    | |      | |    | |\  /| |    |  _| _                              
   _| |_    _| |_  _| |_\/_| |_  _| |__/ |                             
  |_____|  |_____||_____||_____||________|                             
""")
    print("         Press Enter to start...")
    input()  # Wait for user to press Enter
    while True:
        result = input("Hello, Type Enter or type 'Tutorial' for a tutorial, " \
        "type 'Load' to load saved game: ")
        match result.strip().lower().strip():
            case "enter":
                USERNAME = input("Enter your name: ")
                #Saves the PLAYER's name as USERNAME
                PLAYER = playerdata(USERNAME)
                input()
                #Uses time.sleep to wait for 2,5, etc seconds before printing the next text
                print("You woke up in a strange place, with no memory of how you got there.")
                input()
                print("You look around and see a path leading into the distance.")
                input()
                print("You decide to follow it, hoping to find some answers.")
                input()
                print("As you walk, you notice the surroundings changing. " \
                      "The path becomes narrower, "
                      "and the trees around you grow taller and denser. " \
                      "You feel a sense of unease but continue on.")
                input()
                print('Suddenly, you hear a rustling sound behind you. ' \
                      'You turn around quickly, but there is nothing there. ')
                input()
                print('You shake your head, trying to dismiss the feeling of being watched.')
                input()
                print('You can leave or continue on your journey.')
                choice = input("What do you want to do (Leave/Continue)? ")
                #Saves player input as choice
                match choice.strip().lower().strip():
                    case "leave":
                        print("You chose not to continue. " \
                              "You sit down waiting for something to happen.")
                        input()
                        print("Nothing happen, You die of boredom")
                        input()
                        death()
                #This kills the PLAYER since they typed in that they want to leave
                    case "continue":
                        print("You chose to continue. Moving forward...")
                        save_game()
                        companion_chapter()
                #This continues to the next chapter
                    case _:
                        print("Invalid Option")
                        input()
                        print("Try Again")
                #This makes the PLAYER try again
        #This is the option when the PLAYER types in enter or presses enter
            case "tutorial":
                #Gives tutorial to the player
                print("This will restart the game!")
                input()
                print("This is a text based game.")
                input()
                print("Normally, you will wait 5 seconds until the next text loads.")
                input()
                print("If there is a question, " \
                      "type a response that is shown on the screen, "
                      "or you will have to try again.")
                input()
                print("If you choose a bad option, " \
                      "then you would most likely die to reflect what would happen in real life.")
                input()
                print("There a 5 Bosses to beat as well as 3 secret bosses.")
                input()
                print("Remember, this game requires patience so don't"
                      "press anything until it says so!")
                input()
                print("Also, the game will autosave progress onto a " \
                      "JSON file after you complete a chapter."
                      "So if you die, you can still go back to your progress!")
                input()
                print("THIS DOESN'T SAVE ANY PROGRESS IF YOU HAVENT FINISHED THE FIRST CHAPTER")
                input()
                print("To do that type 'Load' on the Welcome text."
                      "That will bring back your progress!")
                input()
                print("Good Luck!")
                main()
                return
        #This shows how to play the game and how the game works
            case "load":
                load_game()
                return
        #This loads when the game last saved
            case _:
                print("Invalid Option, Try again")
                main()
                return
        #This shows when the PLAYER doesn't type in an appropriate response

def companion_chapter():
    """
    Introduces companion to you through a fight
    """
    global COMPANION, CURRENT_CHAPTER
    CURRENT_CHAPTER = "companion_chapter"
    input()
    print("Suddenly, out of the blue, a mysterious character " \
          "jumps out from a bush holding a dagger ready to attack you.")
    input()
    companion_choice = input("You can either type 'Kill' to kill him or " \
                             "type 'Reason' to reason with him: ")
    #Saves the PLAYER's input as companion_choice
    if companion_choice.strip().lower() == "kill":
        print("You tried killing the mysterious character " \
              "but they proceed to strike you in the stomach.")
        input()
        print("You fall to the ground, " \
              "bleeding out and unable to move...")
        input()
        print("The mysterious character stands over you, " \
              "looking down with a mix of pity and regret.")
        input()
        print("You realize that you have made a grave mistake, "
              "and your life is now forfeit.")
        input()
        decrease_health()
        print("You pass out from the pain and lose consciousness.")
        time.sleep(10)
        print("When you wake up you find yourself in a cave resting " \
              "on the floor with the mysterious character standing nearby.")
        input()
        print("He notices you are awake and runs off into the darkness, " \
              "leaving you alone in the cave.")
        input()
        print("You died of loneliness and despair.")
        death()
        return
    #This kills the PLAYER when they try to kill the enemy
    elif companion_choice.strip().lower() == 'reason':
        print("Reasoning with the mysterious character, " \
              "you explain that you mean no harm and are also lost in this strange place...")
        time.sleep(10)
        print("The mysterious character agrees and joins you on your " \
              "journey to get out of this foreign place.")
        input()
        print("The mysterious character is now your Companion.")
        input()
        print("Before continuing, you ask the mysterious character his name.")
        COMPANION = input("Enter Companion's name: ")
        #Saves player input as COMPANION to then be used throughout the game
        save_game()
        chapter_1()
        return
    #This continues the game since the PLAYER wants to reason with
    # COMPANION which is integral to the story
    else:
        death()
        return
    #This shows up when the PLAYER doesn't type an appropriate response

def chapter_1():
    """
    Companion needs help to find their stuff before telling you about Fargon
    """
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_1"
    print(f"***************************\n"
         f"Chapter 1: {COMPANION}'s Dilemma\n"
           "***************************\n")
    input()
    print(f'You and {COMPANION} continue down the path, discussing your situation.')
    input()
    print(f"'You know, I know a way out of here, but I need your help first,' :{COMPANION}.")
    input()
    dagger_choice = input("During our little scuffle, I lost my dagger."
                          f"Can you help me find it? :{COMPANION}(Yes/No): ")
    #Saves the PLAYER's input as dagger_choice
    if dagger_choice.strip().lower() == "yes":
        print(f"Thank you! I knew I could count on you! :{COMPANION}")
        input()
        print(f"You and {COMPANION} start searching the area for the lost dagger.")
        time.sleep(10)
        print("After a while, you find the dagger hidden under some leaves.")
        input()
        print(f"You hand the dagger back to {COMPANION}, who looks relieved.")
        input()
        print(f"Here, {USERNAME} take my dagger,"
              f"I see you have no weapon. Follow me, {USERNAME}. :{COMPANION}")
        input()
        print(f"You acquired {COMPANION}'s trusty dagger.")
        input()
        print(SPECIAL_DAGGER)
        input()
        save_game()
        chapter_2()
        return
    #This continues the game since the PLAYER wants to help COMPANION
    else:
        print(f"Too bad, I guess you don't want to leave this place... :{COMPANION}")
        time.sleep(10)
        print(f"{COMPANION} turns away and walks off into the darkness, leaving you alone.")
        input()
        print("You died of loneliness and despair.")
        death()
        return
    #This kills the PLAYER since they don't want to help

def chapter_2():
    """
    Companion tells you about the backstory of Fargon
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_2"
    print("***************************\n"
       "Chapter 2: The Lost Princess of Faron\n"
          "***************************\n")
    input()
    print("Ok, so you see, This place is called Faron,"
            "it used to be a beautiful place,"
          f"ruled by a princess called Violet. :{COMPANION}")
    input()
    print("But now, it's just a shadow of its former self,"
          f"plagued by dark creatures and monsters. :{COMPANION}")
    input()
    print(f"As you and {COMPANION} walk, you can feel"
           "the weight of the history around you.")
    input()
    print("You see ruins of old buildings, broken statues, "
          "and remnants of a once-thriving civilization in the distance.")
    input()
    print(f"You ask {COMPANION} about Princess Violet and what happened to her.")
    input()
    print(f"{COMPANION} looks sad 'The princess was taken by"
          f"the monsters that consumed this place. :{COMPANION}")
    input()
    print(f"She was the last hope for Faron, but now she's gone. :{COMPANION}")
    input()
    print("You feel a sense of determination to find a way to save Faron and its lost princess.")
    input()
    print(f"You ask {COMPANION} how do they know all this.")
    input()
    print("'I arrived a few years ago, and I have been trying"
          f"to find a way out ever since. :{COMPANION}'")
    input()
    print("I have heard stories from the locals about the princess"
          f"and the monsters that took her. :{COMPANION}")
    input()
    print(f"You ask {COMPANION} where the princess is at now?")
    input()
    print("I don't know, but I have heard rumors of a hidden temple deep in the forest." /
          "It's said that the princess is trapped there,"
          f"guarded by powerful creatures. :{COMPANION}")
    input()
    path_choice = input("You have a choice to make." \
                        "Do you want to go to the temple and try " \
                        "to rescue the princess? (Yes/No): ")
    if path_choice.strip().lower() == "yes":
        print(f"You and {COMPANION} set off towards the hidden temple,"
              "determined to rescue the princess.")
        #Saves the PLAYER's input as path_choice
        input()
        save_game()
        input()
        chapter_3()
        return
    #This goes to the next chapter since the PLAYER wants to progress
    else:
        print("You decide not to take the risk and continue on your current path.")
        input()
        print("All of a sudden, you hear a loud roar and a bull appears out of nowhere.")
        input()
        print(BULL)
        input()
        bull_fight = input("You can either type 'Run' to run away or " \
                           "type 'Fight' to fight the bull: ")
        #Saves the PLAYER's input as bull_fight
        if bull_fight.strip().lower() == "run":
            print("You turn and run as fast as you can, escaping the bull's charge.")
            input()
            print("Unfortunately, you run into a dead end and the bull catches up to you.")
            input()
            death()
            return
        #This kills the PLAYER as the bull kills them
        elif bull_fight.strip().lower() == "fight":
            print("You bravely stand your ground and prepare to fight the bull.")
            input()
            print("You regret your choice")
            input()
            death()
            return
        #This also kills the PLAYER as the bull kills them
        else:
            print("Invalid choice. The bull charges at you!")
            death()
            return
        #This also kills the PLAYER
    #This goes to the bull scene where all the options kill the PLAYER

def chapter_3():
    """
    Introducs the mechanics and what the battles will feel like, with the first dungeon
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_3"
    while True:
        print("***************************\n"
              "Chapter 3: The Hidden Temple\n"
              "***************************\n")
        #Introduction to the dungeon
        input()
        print(DUNGEON_1)
        #This prints the ascii art for the dungeon
        print(f"You and {COMPANION} arrive at the hidden temple,"
              "its entrance shrouded in vines and darkness.")
        input()
        print("As you step inside, you feel a chill run down your spine. " \
              "The air is thick with dust and the smell of decay.")
        input()
        print("You can hear the faint sound of water dripping in the distance, " \
              "echoing through the empty halls.")
        input()
        print(f"You and {COMPANION} cautiously explore the temple,"
              "searching for any signs of the princess.")
        input()
        print(f"Here, {USERNAME} take this sword as well as this shield,"
              f"Stay cautious, I don't have a good feeling about this... :{COMPANION}")
        input()
        print(f"You have acquired {COMPANION}'s special iron sword and reinforced shield")
        input()
        print(SPECIAL_SWORD)
        input()
        print(SPECIAL_SHIELD)
        input()
        print("Suddenly, you hear a loud roar and a " \
              "giant creature appears in front of you, blocking your path.")
        input()
        print("The creature is a massive stone golem, its eyes glowing with an eerie light.")
        input()
        print(f"All of a sudden, the golem charges at {COMPANION} and knocks them to the wall")
        input()
        print("****************************\n"
              " Forging The Beast of Stone \n"
              "****************************\n")
        #Introduction to the boss
        print(GOLEM)
        #This prints the ascii for the golem, this repeats for all the bosses
        input()
        print("You have a choice to make. Do you want to fight the golem "
              "or try to reason with it? (Fight/Reason): ")
        golem_choice = input("What do you want to do? ")
        #Saves the PLAYER's input as golem_choice
        if golem_choice.strip().lower() == "fight":
            print("You bravely stand your ground and prepare to fight the golem.")
            input()
            print("It charges at you, swinging its massive fists.")
        #This continues to the next attack sequence
        elif golem_choice.strip().lower() == "reason":
            print("You try to reason with the golem, explaining that " \
                  "you mean no harm and are only looking for the princess.")
            input()
            print("Never do that again, the golem doesn't speak English, it does speak with fists")
            input()
            print("The golem knocks you out cold")
            input()
            death()
            return
        #This kills the PLAYER since they tried reasoning with a rock
        else:
            print("Invalid choice. The golem charges at you!")
            input()
            death()
            return
        #This kills the PLAYER since they did an invalid response
        while True:
            golem_choice2 = input("You can either type 'Dodge' to dodge its attack "
                                  "or type 'Attack' to attack it: ")
            #Saves the PLAYER's input as golem_choice2
            if golem_choice2.strip().lower() == "dodge":
                print("You quickly dodge the golem's attack, narrowly avoiding its powerful fists.")
                input()
                print("You counterattack, striking the golem with all your might.")
                input()
                print("The golem staggers back, but it is not defeated yet."
                      f"You and {COMPANION} must work together to defeat it.")
                input()
                save_game()
                chapter_3part2()
                return
            #This continues to the next chapter
            elif golem_choice2.strip().lower() == "attack":
                print("You charge at the golem, swinging your weapon with all your might.")
                input()
                print("The golem retaliates with a powerful punch, " \
                      "sending you flying across the room.")
                input()
                death()
                return
            #This kills the PLAYER
            else:
                print("Invalid choice. The golem charges at you!")
                input()
                death()
                return
            #This kills the PLAYER for an invalid response

def chapter_3part2():
    """
    Part 2 of Chapter 3, battle continues
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_3part2"
    while True:
        golem_choice3 = input("You can either type 'Attack' to attack the golem again"
                              f"or type 'Heal' to wake up {COMPANION}: ")
        #Saves the PLAYER's input as golem_choice3
        if golem_choice3.strip().lower() == "attack":
            print(f"You and {COMPANION} attack the golem with all your might.")
            input()
            print("The golem stands unfazed, cracks form but it is still standing.")
            input()
            print("You realize that you need to find a way to weaken it before you can defeat it.")
        #This repeats the question again
        elif golem_choice3.strip().lower() == "heal":
            print(f"You use a healing potion to wake up {COMPANION}.")
            input()
            print(f"{COMPANION} is back in the fight!")
            print("You both attack the golem together, striking it with all your might.")
            input()
            print("The golem staggers back, its stone body cracking under your combined assault.")
            input()
            print("You both continue to attack the golem, striking it with all your might.")
            input()
            print("Finally, with one last powerful blow, " \
                  "the golem crumbles to the ground, defeated.")
            input()
            print(f"You and {COMPANION} stand victorious,"
                   "breathing heavily from the intense battle.")
            input()
            print("You search the golem's remains and find a rusty grey key " \
                  "that unlocks a hidden door in the temple.")
            input()
            print(f"You and {COMPANION} enter the hidden door, hoping to find the princess inside.")
            input()
            print("As you step through the door, you find yourselves in " \
                  "a dimly lit chamber filled with ancient artifacts.")
            input()
            print("In the center of the room, you see a pedestal with a glowing golden key.")
            input()
            print("****************************\n"
                  "  1 Key Achieved 4 left. \n"
                  "****************************\n")
            save_game()
            chapter_4()
            return
        #This shows you've defeated the boss and have gained a key
        else:
            print("Invalid choice. Try again.")
        #This repeats the question

def chapter_4():
    """
    Tells more backstory about the keys
    """
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_4"
    while True:
        print("***************************\n"
              "Chapter 4: The Path Ahead\n"
              "***************************\n")
        input()
        print(f"You and {COMPANION} exit the temple past the pile of"
               "rubble and continue down a path.")
        input()
        key_question = input(f"You can ask {COMPANION} a question about the other keys"
                              "or continue down the path playing with the key. (Ask/Continue): ")
        #Saves the PLAYER's input as key_question
        if key_question.strip().lower() == "ask":
            print(f"You ask {COMPANION} about the other keys.")
            input()
            print(f"'There are 5 keys in total, but I don't know the exact locations,"
                  f"but I have heard rumors of their existence' :{COMPANION}")
            input()
            print("Suddenly, the key shifts in you hand and points forwards.")
            input()
            print(f"You thank {COMPANION} for the information and continue down the path.")
            input()
            print(f"The path ahead changes to a lush green tropical forest but you and"
                  f"{COMPANION} are determined to find the other keys and rescue the princess.")
            save_game()
            chapter_5()
            break
        #This continues to the next dungeon while showing a little more backstory
        elif key_question.strip().lower() == "continue":
            print("You decide to continue down the path, playing with the key you found.")
            input()
            print("The key feels warm in your hand, and you can sense its power.")
            input()
            print(f"The path ahead changes to a lush green tropical forest but you and {COMPANION}"
                   "are determined to find the other keys and rescue the princess.")
            save_game()
            input()
            save_game()
            chapter_5()
            break
        #This skips the backstory but still goes to the next dungeon
        else:
            print("Invalid choice, Try again")
        #This asks the question again in a loop until they ask a valid response
#This is to bring a small break between the dungeons

def chapter_5():
    """
    Introduces the goblin camp and the next dungeon
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_5"
    print("***************************\n"
          "Chapter 5: The Goblin Camp\n"
          "***************************\n")
    input()
    print(f"You and {COMPANION} arrive at the goblin camp,"
           "a makeshift settlement hidden deep in the forest.")
    input()
    print("As you enter, you can feel the tension in the air. " \
          "The goblins eye you suspiciously, their weapons at the ready.")
    input()
    print("You know that this will be a difficult challenge, " \
          "but you are determined to find the next key.")
    input()
    print("We need to be careful."
          f"The goblins are known for their traps and ambushes. :{COMPANION}")
    input()
    print("You nod in agreement and start to plan your approach.")
    input()
    print(f"Stay here, I'll go talk to the camp chief"
          f"and see if they know anything about the key. :{COMPANION}")
    input()
    print(f"{COMPANION} disappears around the corner of a hut, leaving you alone in the camp.")
    input()
    goblin_choice = input("Now you have a choice to make."
                          f"Do you want to wait for {COMPANION} to return"
                           "or explore the camp on your own? (Wait/Explore): ")
    #Saves the PLAYER's input as goblin_choice
    if goblin_choice.strip().lower() == "wait":
        print(f"You decide to wait for {COMPANION} to return.")
        input()
        print(f"{COMPANION} returns after a while, looking worried.")
        input()
        print("The goblin chief knows where the dungeon is,"
              f"but he won't give it up easily. :{COMPANION}")
        input()
        print(f"You approach the chief with {COMPANION}")
        input()
        goblin_choice2 = input("Do you want to try to reason with " \
                               "the goblin chief or attack him? (Reason/Attack): ")
        while True:
    #Waiting for COMPANION to come back and the going to the chief
            if goblin_choice2.strip().lower() == "reason":
                print(f"You and {COMPANION} approach the goblin chief, trying to reason with him.")
                input()
                print("The goblin chief listens to your plea, but he is not convinced.")
                input()
                print(f"We need to find another way to get the location :{COMPANION}")
                input()
                print("You nod in agreement and start to plan your next move.")
                input()
                print("You decide to explore the camp further, " \
                      "hoping to find some clues about the location.")
                input()
        #loops again to the goblin chief question
            elif goblin_choice2.strip().lower() == "attack":
                print(f"You and {COMPANION} decide to attack the goblin chief.")
                input()
                print("The goblin chief fights back fiercely, " \
                      "but you manage to defeat him after a tough battle.")
                input()
                print("You search the goblin chief's hut and find a map " \
                      "that leads to the next dungeon.")
                input()
                print(f"You and {COMPANION} take the map and prepare to continue your journey.")
                save_game()
                chapter_6()
                return
         #Goes to next chapter after you attack him
            else:
                print("Invalid choice. Try again")
        #For invalid choices which then repeats
    elif goblin_choice() == "explore":
        while True:
            print("You decide to explore the camp on your own.")
            input()
            print("As you look around, you notice a few goblins eyeing you suspiciously.")
            input()
            print("Nonetheless, you continue to explore, hoping to find some clues about the key.")
            input()
            print("You find a small windmill with a sign that reads 'Storage Space'.")
            input()
            print(GOBLIN_HUT)
            goblin_choice3 = input("Do you want to enter the windmill? (Yes/No): ")
            if goblin_choice3.strip().lower() == "yes":
            #Saves the PLAYER's input as goblin_choice3
                while True:
                    input()
                    print("You enter the hut and find a chest in the corner.")
                    input()
                    print("You open the chest and find a dusty yellow map inside.")
                    input()
                    print("You take the map and return to the main camp area.")
                    input()
                    print(f"You find {COMPANION} waiting for you, looking relieved.")
                    input()
                    print(f"I was worried about you."
                          f"Did you find anything useful? :{COMPANION}")
                    input()
                    print(f"You show {COMPANION} the map you found in the hut.")
                    input()
                    print(f"{COMPANION} looks at the map"
                          "This looks like to the next dungeon"
                          f"It might help us find the key! :{COMPANION}")
                    save_game()
                    chapter_6()
                    break
            #Goes to the dungeon
            elif goblin_choice3.strip().lower() == "no":
                print("You decide not to enter the windmill and continue exploring the camp.")
                input()
                print("You wander around, but you don't find anything else of interest.")
                input()
                print("You return to the main camp area,"
                      f"where you find {COMPANION} waiting for you.")
                input()
                print(f"Did you find anything useful? :{COMPANION}")
                input()
                print(f"You tell {COMPANION} that you didn't find anything,"
                      "but you feel like you might have missed something important.")
                input()
                print("We should keep looking."
                      f"The goblins might have more information about the key. :{COMPANION}")
             #Loops again and goes back to the question
            else:
                print("Invalid choice.")
          #For invalid choices
#For exploring the goblin camp

    else:
        print("Invalid choice.")
        return
#If the PLAYER does not enter a valid choice

def chapter_6():
    """
    Introduces the second dungeon and the next boss
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_6"
    while True:
        print("***************************\n"
            "Chapter 6: The Crystal Dungeon\n"
              "***************************\n")
        input()
        print(DUNGEON_2)
        input()
        print(f"You and {COMPANION} arrive at the entrance of the lush green cavern,"
              "the second dungeon.")
        input()
        print("The air is thick with moisture, "
              "and you can hear the sound of dripping water echoing through the darkness.")
        input()
        print("You light a torch and step inside, " \
              "the flickering light revealing jagged rocks and narrow passages.")
        input()
        print("Be careful. This place is known for its"
              f"traps and dangerous creatures. :{COMPANION}")
        input()
        print("You nod and start to explore the cavern, searching for the key.")
        input()
        print("As you venture deeper, you come across a large underground lake.")
        input()
        print("In the center of the lake, you see a small island with a pedestal on it.")
        input()
        print("On the pedestal, you can see a glimmering blue key.")
        input()
        print(f"You and {COMPANION} realize that this must be the second key you are looking for.")
        input()
        print("Before either of you could react, " \
              "a giant beast emerges from the water, its eyes glowing with a menacing light.")
        input()
        print("The beast is a massive serpent, its scales glistening in the water")
        input()
        print("****************************\n"
              "Serpus The Beast of the Lake \n"
              "****************************\n")
        print(SERPUS)
        #Shows ascii art of the serpus
        input()
        print("Before either of you could move, Serpus strikes you both in the back.")
        decrease_health()
        print(f"{COMPANION}'s health is low")
        input()
        serpent_choice = input("Serpus is charging up it's next attack, (Attack/Dodge): ")
        #User's input is stored as serpent_choice
        if serpent_choice.strip().lower() == "attack":
            print("Serpus strikes you in the stomach and injures you.")
            input()
            decrease_health()
            print(f"{COMPANION}'s health is low")
            input()
            print(f"You and {COMPANION} are both injured"
                  "and need to find a way to defeat Serpus before it attacks again.")
            input()
            save_game()
            serpus_fight3()
        #Goes to next the final sequence
        elif serpent_choice.strip().lower() == "dodge":
            print("You quickly dodge Serpus's attack, narrowly avoiding its powerful strike.")
            input()
            print("You counterattack, striking Serpus with all your might.")
            input()
            print("The serpent staggers back,"
                  "but it is not defeated yet."
                  f"You and {COMPANION} must work together to defeat it.")
            input()
            save_game()
            serpus_fight2()
        #Goes to the next sequence
        else:
            print("Invalid choice. Serpus attacks you again!")
            death()
        #Kills the PLAYER since they didn't respond properly

def serpus_fight2():
    """    
    Continues the fight with Serpus
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "serpus_fight2"
    while True:
        serpent_choice2 = input("You can either type 'Attack' to attack Serpus"
                                f"or type 'Heal' to heal yourself and {COMPANION}: ")
        #User's input is stored as serpentchoice2
        if serpent_choice2.strip().lower() == "attack":
            print(f"You and {COMPANION} attack Serpus with all your might,"
                  "striking it with your weapons.")
            input()
            print("Finally, with one last powerful blow, " \
                  "Serpus roars in pain and sinks back into the depths of the lake.")
            input()
            print(f"You and {COMPANION} stand victorious,"
                  "breathing heavily from the intense battle.")
            input()
            print("You search the serpent's remains and find a glimmering blue key " \
                  "that unlocks a hidden door in the cavern.")
            input()
            print(f"You and {COMPANION} enter the hidden door,"
                  "hoping to find the next key inside.")
            input()
            print("As you step through the door, " \
                  "you find yourselves in a dimly lit chamber filled with ancient artifacts.")
            input()
            print("In the center of the room, you see a pedestal with a glowing blue key.")
            input()
            print("****************************\n"
                   "  2 Key Achieved 3 left. \n"
                  "****************************\n")
            print(f"You and {COMPANION} take the key and prepare to continue your journey.")
            input()
            save_game()
            dark_dagger_story()
            #Shows the dagger upgrade story
            return
        elif serpent_choice2.strip().lower() == "heal":
            print(f"You use a healing potion to heal yourself and {COMPANION}.")
            input()
            print(f"{COMPANION} is back in the fight!")
            input()
            print("You both attack Serpus together, striking it with all your might.")
            input()
            print("Serpus slithers back, its slimy scales cracking under your combined assault.")
            input()
            print("You both continue to attack Serpus, striking it with all your might.")
            input()
            print("Finally, with one last powerful blow, Serpus collapses to the ground, defeated.")
            input()
            print(f"You and {COMPANION} stand victorious,"
                  "breathing heavily from the intense battle.")
            input()
            print("You search Serpus's remains and find a mysterious " \
                  "blue key that unlocks a hidden door in the temple.")
            input()
            print(f"You and {COMPANION} enter the hidden door, hoping to find the princess inside.")
            input()
            print("As you step through the door, you find yourselves "
                  "in a dimly lit chamber filled with ancient artifacts.")
            input()
            print("In the center of the room, you see a pedestal with a glowing blue key.")
            input()
            print("****************************\n"
                   "  2 Key Achieved 3 left. \n"
                  "****************************\n")
            print(f"You and {COMPANION} take the key and prepare to continue your journey...")
            input()
            save_game()
            dark_dagger_story()
            #This shows the dagger upgrade story
            return
        else:
            print("Invalid choice. Serpus attacks you again!")
            death()
            break
        #This kills the PLAYER since they entered an invalid response

def serpus_fight3():
    """
    Final fight sequence with Serpus
    """
    global CURRENT_CHAPTER
    # These are global variables for the saving function,
    # PLAYER USERNAME, PLAYER stats, COMPANION USERNAME
    # allowing for these functions to work within the different chapters
    CURRENT_CHAPTER = "serpus_fight3"
    #Saves curent chapter
    serpent_choice3 = input("Type 'Attack' to attack Serpus again or"
                            f"type 'Heal' to heal yourself and {COMPANION}: ")
    if serpent_choice3.strip().lower() == "attack":
        print(f"You and {COMPANION} attack Serpus's core with all your might,"
              "striking it with your weapons.")
        input()
        print("Serpus roars in pain, and it smashes into the ground, defeated.")
        input()
        print(f"You and {COMPANION} stand victorious, breathing heavily from the intense battle.")
        input()
        print("You search the serpent's remains and find a glimmering " \
              "blue key that unlocks a hidden door in the cavern.")
        input()
        print(f"You and {COMPANION} enter the hidden door, hoping to find the next key inside.")
        input()
        print("As you step through the door, you find yourselves "
              "in a dimly lit chamber filled with ancient artifacts.")
        input()
        print("In the center of the room, you see a pedestal with a glowing blue key.")
        input()
        print("****************************\n"
              "  2 Key Achieved 3 left. \n"
              "****************************\n")
        print(f"You and {COMPANION} take the key and prepare to continue your journey...")
        input()
        save_game()
        dark_dagger_story()
        chapter_7()
            #This shows the dagger upgrade story
    elif serpent_choice3.strip().lower() == "heal":
        print(f"You use a healing potion to heal yourself and {COMPANION}.")
        print("Serpus lunges at you before either of you could attack.")
        death()
        #This kills the PLAYER
    else:
        print("Invalid choice. Serpus attacks you again!")
        death()
        #This kills the PLAYER since they entered an invalid response

def chapter_7():
    """
    Introduces the next chapter and the next dungeon
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_7"
    print("***************************\n"
    "Chapter 7: The Path to the Fire Dungeon\n"
          "***************************\n")
    input()
    print(f"You and {COMPANION} exit the jungle cavern and continue down the path,"
          "the lush greenery giving way to rocky terrain.")
    input()
    print("The air grows hotter, and you can feel the heat radiating from the ground.")
    input()
    print("The next key is said to be hidden in a fire dungeon,"
          f"deep within the mountains according to the map. :{COMPANION}")
    input()
    print("You nod in agreement, determined to find the next key and rescue the princess.")
    input()
    print("As you continue down the path, you come across a group of goblins blocking your way.")
    input()
    print("The goblins are armed with crude weapons and look ready for a fight.")
    input()
    print("We need to be careful."
          f"The goblins are known for their traps and ambushes. :{COMPANION}")
    input()
    goblin_offer = input("Do you want to fight the goblins "
                         "or try to reason with them? (Fight/Reason): ")
    if goblin_offer.strip().lower() == "fight":
        print(f"You and {COMPANION} charge at the goblins, weapons drawn.")
        input()
        print("The goblins fight back fiercely,"
              f"but you and {COMPANION} are able to defeat them after a tough battle.")
        input()
        print("You search the goblins' remains and find a map that leads to the fire dungeon.")
        input()
        print(f"You and {COMPANION} take the map and prepare to continue your journey.")
        input()
        save_game()
        chapter_8()
        #This moves to the next chapter
    elif goblin_offer.strip().lower() == "reason":
        print("You try to reason with the goblins, " \
              "explaining that you mean no harm and are only looking for the next key.")
        input()
        print("The goblins listen to your words, but they are still wary of you.")
        input()
        print(f"{COMPANION} suggests that you offer them something in exchange for safe passage.")
        input()
        goblin_offer2 = input("Do you want to offer them some of your supplies? (Yes/No): ")
        if goblin_offer2.strip().lower() == "yes":
            print("You offer the goblins some of your supplies, and they accept your offer.")
            input()
            print(f"The goblins allow you and {COMPANION}"
                  "to pass safely, and you continue on your journey.")
            input()
            save_game()
            chapter_8()
        #This moves to the next chapter
        elif goblin_offer.strip().lower() == "no":
            print("The goblins refuse to let you pass without a fight.")
            input()
            print(f"You and {COMPANION} are forced to fight the goblins,"
                   "but you are able to defeat them after a tough battle.")
            input()
            decrease_health()
            input()
            print("You search the goblins' sacks and find a map that leads to the fire dungeon.")
            input()
            print(f"You and {COMPANION} take the map and prepare to continue your journey.")
            input()
            save_game()
            chapter_8()
        #This moves to the next chapter
        else:
            print("Invalid choice. You continue down the path without making a decision.")
            input()
            save_game()
            chapter_8()
            return
    else:
        print("Invalid choice. You continue down the path without making a decision.")
        input()
        save_game()
        chapter_8()
        return
        #This moves to the next chapter

def chapter_8():
    """
    Introduces the fire dungeon and the next boss
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_8"
    print("***************************\n"
          "Chapter 8: The Fire Dungeon\n"
          "***************************\n")
    input()
    print(DUNGEON_3)
    input()
    print(f"You and {COMPANION} arrive at the entrance of the fire dungeon,"
          "a dark cave filled with molten lava and fire.")
    input()
    print("The heat is intense, and you can feel the sweat pouring down your face.")
    input()
    print(f"Be careful. This place is known for its lava creatures :{COMPANION}")
    input()
    print("You nod and start to explore the dungeon, searching for the key.")
    input()
    print("As you venture deeper, you come across a large underground chamber filled with lava.")
    input()
    print("In the center of the chamber, you see a small island with a pedestal on it.")
    input()
    print("On the pedestal, you can see a glowing red key.")
    input()
    print(f"You and {COMPANION} realize that this must be the third key you are looking for.")
    input()
    print("Before either of you could react, a giant beast emerges from the lava,"
          "its eyes glowing with a menacing light.")
    input()
    print("The beast is a massive fire phoenix, its body made of pure flame.")
    input()
    print("****************************\n"
          "  flame The Beast of Fire \n"
          "****************************\n")
    print(FLAME)
    # This prints the ascii art for flame
    # Dragon choice is used as flame was originally a dragon
    # but was changed to a phoenix mid way through
    input()
    phoenix_choice = input("flame starts charging up it's attack! (Attack/Dodge): ")
    input()
    decrease_health()
    input()
    if phoenix_choice.strip().lower() == "attack":
        print("flame breathes fire at you, before either of " \
              "you could attack scorching your skin and leaving you in pain.")
        input()
        decrease_health()
        print(f"{COMPANION}'s health is low")
        input()
        print(f"You and {COMPANION} are both injured and need to"
              "find a way to defeat flame before it attacks again.")
        input()
        phoenix_choice2 = input("You can either type 'Attack' to attack"
                                f"flame or type 'Heal' to heal yourself and {COMPANION}: ")
        if phoenix_choice2.strip().lower() == "attack":
            print(f"You and {COMPANION} attack flame with all your might,"
                  "striking it with your weapons.")
            input()
            print("flame roars in pain, but it is not defeated yet.")
            input()
            phoenix_choice3 = input("Type 'Attack' to attack flame again or"
                                    f"type 'Heal' to heal yourself and {COMPANION}: ")
            while True:
            #A loop is used to allow the PLAYER to restart at select points
                if phoenix_choice3.strip().lower() == "attack":
                    print(f"You and {COMPANION} attack flame with all your might.")
                    input()
                    print("flame roars in pain, but it is not defeated yet.")
                    input()
                    print("flame spews out lava, and melts you and COMPANION")
                    input()
                    death()
                    break
                #This kills the PLAYER
                elif phoenix_choice3.strip().lower() == "heal":
                    print(f"You use a healing potion to heal yourself and {COMPANION}.")
                    increase_health(50)
                    input()
                    print(f"{COMPANION} is back in the fight!")
                    input()
                    print("You both attack flame together, striking it with all your might.")
                    input()
                    print("flame roars in pain, it's hardened feathers are " \
                          "starting to crack under your combined assault.")
                    phoenix_choice4 = input("Type 'Attack' to attack flame again or"
                                            f"type 'Heal' to heal yourself and {COMPANION}: ")
                    if phoenix_choice4.strip().lower() == "attack":
                        print(f"You and {COMPANION} attack flame's core"
                              "with all your might, striking it with your weapons.")
                        input()
                        print("flame roars in pain, and it crumbles to the ground, defeated.")
                        input()
                        print(f"You and {COMPANION} stand victorious,"
                              "breathing heavily from the intense battle.")
                        input()
                        print("You search the dragon's remains and find a glowing " \
                              "red key that unlocks a hidden door in the dungeon.")
                        input()
                        print(f"You and {COMPANION} enter the hidden door,"
                              "hoping to find the next key inside.")
                        input()
                        print("As you step through the door, you find yourselves "
                              "in a dimly lit chamber filled with ancient artifacts.")
                        input()
                        print("In the center of the room, you see a pedestal with a " \
                              "glowing red key.")
                        input()
                        print("****************************\n"
                               "  3 Key Achieved 2 left. \n"
                              "****************************\n")
                        save_game()
                        input()
                        dark_sword_story()
                        input()
                        chapter_9()
                        break
                #This shows the sword upgrade story
                #This moves to the next chapter
                elif phoenix_choice3.strip().lower() == "heal":
                    print(f"You use a healing potion to heal yourself and {COMPANION}.")
                    input()
                    print(f"{COMPANION} is back in the fight!")
                    input()
                    print("flame attacks you before you can attack again!")
                    input()
                    print(f"You and {COMPANION} are both injured and"
                          "need to find a way to defeat flame before it attacks again.")
                    decrease_health(50)
                    input()
                    print(f"{COMPANION}'s health is low")
                    input()
                    print("flame attacks you before you can attack again!")
                    death()
                    return
                #This kills the PLAYER
                else:
                    print("Invalid choice. flame attacks you again!")
                    death()
                    return
                #This kills the PLAYER since they didn't provide an appropriate response
        elif phoenix_choice2.strip().lower() == "heal":
            print(f"You use a healing potion to heal yourself and {COMPANION}.")
            increase_health(50)
            input()
            print(f"{COMPANION} is back in the fight!")
            input()
            print("You both attack flame together, striking it with all your might.")
            input()
            print("flame roars in pain, but it's feathers harden under your combined assault")
            input()
            print("flame attacks you before you can attack again!")
            input()
            print("flame charges up another burst of fire,"
                  f"and spews directly at you and {COMPANION}")
            input()
            death()
            return
            #This kills the PLAYER
        else:
            print(f"Invalid option, flame spews hot lava all over you and {COMPANION}.")
            input()
            death()
            return
        #This kills the PLAYER as they entered the wrong input
    elif phoenix_choice.strip().lower() == "dodge":
        print("You quickly dodge flame's attack, narrowly avoiding its powerful strike.")
        input()
        print("You counterattack, striking flame with all your might.")
        input()
        print("The phoenix staggers back, but it is not defeated yet."
              f"You and {COMPANION} must work together to defeat it.")
        input()
        while True:
            phoenix_choice5 = input("You can either type 'Attack' to attack"
                                    "flame again or type 'Heal' to heal"
                                    f"yourself and {COMPANION}: ")
            if phoenix_choice5.strip().lower() == "attack":
                print(f"You and {COMPANION} attack flame with all your might.")
                input()
                print(f"You and {COMPANION} attack flame's core with all your might,"
                      "striking it with your weapons.")
                input()
                print("flame roars in pain, and it crumbles to the ground, defeated.")
                input()
                print(f"You and {COMPANION} stand victorious,"
                      "breathing heavily from the intense battle.")
                input()
                print("You search the dragon's remains and find a " \
                      "glowing red key that unlocks a hidden door in the dungeon.")
                input()
                print(f"You and {COMPANION} enter the hidden door,"
                      "hoping to find the next key inside.")
                input()
                print("As you step through the door, " \
                      "you find yourselves in a dimly lit chamber filled with ancient artifacts.")
                input()
                print("In the center of the room, you see a pedestal with a glowing red key.")
                input()
                print("****************************\n"
                       "  3 Key Achieved 2 left. \n"
                      "****************************\n")
                save_game()
                input()
                dark_sword_story()
                #Displays the sword upgrade story
                input()
                chapter_9()
                break
            #This shows the sword upgrade story
            elif phoenix_choice5.strip().lower() == "heal":
                print(f"You use a healing potion to heal yourself and {COMPANION}")
                input()
                print("But before either of you could attack again. flame attacks you both.")
                death()
                return
            #This kills the PLAYER
            else:
                print("Invalid choice. flame attacks you again!")
                death()
                return
            #This kills the PLAYER due to invalid input
        #This kills the PLAYER due to invalid input
    else:
        print("Invalid choice. flame attacks you again!")
        death()
        return
    #This kills the PLAYER due to invalid input

def chapter_9():
    """
    Introduces the next chapter and the next dungeon
    """
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_9"
    print('***************************\n'
    "Chapter 9: The Path to the Ice Dungeon\n"
          '***************************\n')
    input()
    print(f"You and {COMPANION} exit the fire dungeon and continue down a path,"
          "the heat giving way to a more relaxed meadow atmosphere.")
    input()
    print("You spot a small village in the distance, and you can decide " \
          "to stop there to rest and gather supplies.")
    input()
    print(SMALL_VILLAGE)
    input()
    village_choice = input("Do you want to stop at the village? (Yes/No): ")
    if village_choice.strip().lower() == "yes":
        print(f"You and {COMPANION} decide to stop at the village.")
        input()
        print("Before you you approach the villagers, you notice a " \
              "small shop selling potions and supplies.")
        input()
        print("You decide to enter the shop and see what they have to offer.")
        input()
        print(f"{COMPANION} says, 'Hello, shopkeeper!"
              "Do you have any potions or supplies that could help us on our journey?'")
        input()
        print("The shopkeeper nods and shows you a selection of potions and supplies.")
        input()
        print("Maps, healing potions, and other useful items are available "
              "for purchase but one item catches your eye.")
        input()
        print("A dusty old map that seems to lead to the next dungeon.")
        input()
        print("You ask the shopkeeper about the map, and he tells you that it "
              "is a rare find, but he is willing to sell it to you for a fair price.")
        map_choice = input("You can buy a map for 20 gold coins. Do you want to buy it? (Yes/No): ")
        #User input is stored as mapchoice
        if map_choice.strip().lower() == "yes":
            print(f"You buy the map and give to {COMPANION} to analyze")
            input()
            decrease_gold(20)
            input()
            save_game()
            input()
            village()
            return
        #This stops at the village after buying the map
        else:
            print("You decide not to buy the map and continue down the path without it.")
            input()
            save_game()
            input()
            village()
            return
        #This stops at the village without buying
    elif village_choice.strip().lower() == "no":
        print(f"You and {COMPANION} decide to continue down the path"
              "without stopping at the village.")
        input()
        save_game()
        input()
        save_game()
        input()
        chapter_9part2()
        return
    #This skips the village without reseting health and faces the boss without a full health bar
    else:
        print("Invalid choice. You continue down the path without stopping at the village.")
        input()
        save_game()
        input()
        save_game()
        input()
        chapter_9part2()
        return
    #This is for invalid input


def village():
    """
    Resets the PLAYER's health and sets a checkpoint in the village
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "village"
    print("As you enter the village, you are greeted by friendly " \
          "villagers who offer you food and shelter.")
    input()
    print("This is a nice place to rest and"
          f"gather supplies before we continue our journey. :{COMPANION}")
    input()
    print("You spend some time in the village, " \
          "resting and preparing for the next part of your journey.")
    input()
    reset_health()
    print("You feel refreshed and ready to continue your journey.")
    input()
    print("You thank the villagers for their hospitality and prepare to leave the village.")
    input()
    save_game()
    input()
    chapter_9part2()
#This is for the village bit which resets the PLAYERs health and sets a checkpoint

def chapter_9part2():
    """
    Introduces the next part of chapter 9 and the next dungeon
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_9part2"
    print("***************************\n"
     "Chapter 9 Part 2: The Journey Continues\n"
          "***************************\n")
    input()
    print(f"You and {COMPANION} follow the map's directions, navigating through the mountains.")
    input()
    print(DUNGEON_4)
    input()
    print("After a long journey, you arrive at a crossroad.")
    input()
    print(f"{COMPANION} says, 'Where do we go now?'")
    crossroad_choice = input("Do you want to go left (snowy mountains) "
                             "or right (icy cave)? (Left/Right): ")
    match crossroad_choice.strip().lower().strip():
        case "left":
            print(f"You and {COMPANION} decide to go left towards the snowy mountains.")
            input()
            print("The temperature drops and you can see your breath in the cold air.")
            input()
            print(f"{COMPANION} says, 'We must be close to the ice dungeon.'")
            input()
            print("As you continue, the ground shakes and you are buried under a pile of snow.")
            death()
        #death due to avalanche
        case "right":
            print(f"You and {COMPANION} decide to go right towards the icy cave.")
            input()
            print("Entering the cave, the temperature drops further "
                  "and icicles hang from the ceiling.")
            input()
            print(f"This must be the ice dungeon. We need to be careful. :{COMPANION}")
            input()
            print("You explore the cave and find a locked underground chamber; " \
                  "you need a key to open it.")
            input()
            print(f"We must find the key to unlock this door. :{COMPANION}")
            input()
            print("Searching the chamber, you discover 2 small chests hidden behind a pile of ice.")
            input()
        #No death
            ice_chest_choice = input("Do you want to open the left chest "
                                     "or the right chest? (Left/Right): ")
            while True:
                match ice_chest_choice.strip().lower().strip():
                    case "left":
                        print("You open the left chest and find a shiny key inside!")
                        input()
                        print(f"This must be the door key! :{COMPANION}")
                        input()
                        print("You insert the key into the lock and " \
                              "the door creaks open, revealing the next part of the dungeon.")
                        input()
                        print(f"You and {COMPANION} step through, ready for further challenges.")
                        input()
                        print("An icicle hits you on the head, and you black out.")
                        input()
                        print("When you wake up, you're in a giant icy cavern"
                              f"and {COMPANION} is missing as well as your sword.")
                        input()
                        print("A dirty rag in the corner starts moving, "
                              "and a ghoulish creature emerges.")
                        input()
                        print("*****************************\n"
                                  "Morjun the Ice wraith\n"
                              "*****************************\n")
                        input()
                        print(WRAITH)
                        input()
                        print("Morjun lunges at you, slashing with icy claws.")
                        input()
                        decrease_health()
                        input()
                        print("Stumbling back, you notice a rusty sword nearby.")
                        input()
                        wraith_choice = input("Do you want to pick up the sword and " \
                                              "fight Morjun or try to escape " \
                                              "the cavern? (Fight/Escape): ")
                        match wraith_choice.strip().lower().strip():
                            case "fight":
                                print("You pick up the sword and prepare to fight Morjun.")
                                input()
                                print("You dodge Morjun's attack and strike, " \
                                      "hitting it in the side.")
                                input()
                                while True:
                                    wraith_choice2 = input("Do you want to attack again "
                                                           "or heal yourself? (Attack/Heal): ")
                                    match wraith_choice2.strip().lower().strip():
                                        case "attack":
                                            print("You attack Morjun with all your might, "
                                                  "and it falls to the ground, defeated.")
                                            input()
                                            print("You search Morjun's remains and " \
                                                  "find a glowing ice key that unlocks a door.")
                                            input()
                                            print(f"You open a door and spot {COMPANION}"
                                                    "in a cage.")
                                            input()
                                            print(f"You free {COMPANION} from the cage and carry"
                                                  "them out of the cavern.")
                                            input()
                                            print(f"You and {COMPANION} step out of the cavern"
                                                  "through another door into a dimly lit maze.")
                                            input()
                                            maze_choice = input("Would you like to explore " \
                                                                "the maze or return to the cavern? "
                                                                "(Explore/Return): ")
                                            match maze_choice.strip().lower().strip():
                                                case "explore":
                                                    print(f"You and {COMPANION} decide to explore"
                                                          "the maze for a way out.")
                                                    input()
                                                    maze_choice2 = input("Do you want to go" \
                                                                         "left or right? "
                                                                         "(Left/Right): ")
                                                    match maze_choice2.strip().lower().strip():
                                                        case "left":
                                                            print("You take the left path "
                                                                  "and find a " \
                                                                  "small clearing.")
                                                            input()
                                                            print("In the clearing, a pedestal " \
                                                                  "holds a glowing ice key.")
                                                            input()
                                                            print("****************************\n"
                                                                     "4 Key Achieved 1 left.\n"
                                                                  "****************************\n")
                                                            input()
                                                            save_game()
                                                            input()
                                                            chapter_10()
                                                            break
                                                    #Achieves key and continues to next chapter
                                                        case "right":
                                                            print("You take the right path and end"
                                                                  "in a dead end. Go back!")
                                                            input()
                                                    #Repeats until they choose left
                                                        case _:
                                                            print("Invalid choice. " \
                                                                  "Returning to cavern.")
                                                            input()
                                                            return
                                                    #Goes back to question
                                                case "return":
                                                    print(f"You and {COMPANION}"
                                                          "return to the cavern.")
                                            #Goes back to cavern and repeats
                                                case _:
                                                    print("Invalid choice. Returning to cavern.")
                                                    input()
                                                    return
                                            #Goes back to cavern and repeats
                                        case "heal":
                                            print("You use a healing potion to heal yourself.")
                                            input()
                                            increase_health(50)
                                            input()
                                            print("Unfortunately, you trip and fall leaving " \
                                                  "you in the cave forever.")
                                            input()
                                            death()
                                            return
                                        #death
                                        case _:
                                            print("Invalid choice.")
                                            break
                                    #Repeats the question
                            case "escape":
                                print("You try escaping but Morjun possesses you.")
                                input()
                                death()
                                return
                            #death
                            case _:
                                print("Invalid choice. You trip over a rock.")
                                input()
                                death()
                                return
                            #Gets killed by a rock
                    case "right":
                        print("You open the right chest and find a pile of gold coins.")
                        input()
                        increase_gold(50)
                        input()
                        print(f"Nice find, but we still need the key. :{COMPANION}")
                        input()
                        #Collects coins then loops the question
                    case _:
                        print("Choose a valid option")
                     #Loops the question
        case _:
            print("Invalid choice. Choose again.")
            input()
        #Loops


def chapter_10():
    """
    Introduces the next chapter and the final dungeon
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_10"
    print("***************************\n"
    "Chapter 10: The Path to the Final Dungeon\n"
          "***************************\n")
    input()
    print(f"You and {COMPANION} exit the ice dungeon and continue towards the last dungeon,"
          "the icy terrain giving way to rocky cliffs.")
    input()
    print("The air grows colder, and you can see your breath in the frigid air.")
    input()
    print("The final key is said to be hidden in a dark dungeon,"
          f"deep within the mountains according to the map. :{COMPANION}")
    input()
    print("You nod in agreement, determined to find the final key and rescue the princess.")
    input()
    print("As you continue down the path, you come across a group of trolls blocking your way.")
    input()
    print(TROLL)
    input()
    print("The trolls are armed with large clubs and look ready for a fight.")
    input()
    print(f"{COMPANION} whispers, 'We need to be careful."
          "The trolls are known for their brute"
          "strength and cunning traps.'")
    input()
    troll_choice = input("Do you want to fight the trolls or try " \
                         "to reason with them? (Fight/Reason): ")
    if troll_choice.strip().lower() == "fight":
        print(f"You and {COMPANION} charge at the trolls, weapons drawn.")
        input()
        print(f"The trolls fight back fiercely, but you and {COMPANION}"
              "are able to defeat them after a tough battle.")
        input()
        print("You search the trolls' remains and find a map that leads to the final dungeon.")
        input()
        print(f"You and {COMPANION} take the map and prepare to continue your journey.")
        input()
        save_game()
        input()
        chapter_11()
        input()
    #Continues to next chapter
    elif troll_choice.strip().lower() == "reason":
        print("You try to reason with the trolls, explaining that you " \
              "mean no harm and are only looking for the final key.")
        input()
        print("The trolls try listening to your words, yet they don't speak English.")
        input()
        death()
        return
    #death due to language barrier

def chapter_11():
    """
    Introduces the final dungeon and the final boss
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_11"
    print("***************************\n"
          "Chapter 11: The Final Dungeon\n"
          "***************************\n")
    print(f"You and {COMPANION} arrive at the entrance of the final dungeon,"
          "a dark cave filled with ominous shadows.")
    input()
    print(DUNGEON_5)
    input()
    print("The air is thick with tension, and you can feel the weight of " \
          "the final challenge ahead.")
    input()
    print("This is it. The final key is said to"
          f"be hidden in this dungeon, guarded by a powerful monster. :{COMPANION}")
    input()
    print("You nod, determined to find the final key and rescue the princess.")
    input()
    print("As you venture deeper into the dungeon, you come across " \
          "a large underground chamber filled with darkness.")
    input()
    print("In the center of the chamber, you see a pedestal with a glowing black key.")
    input()
    print("But before you can approach the pedestal, a massive " \
          "shadowy figure emerges from the darkness.")
    input()
    print("The figure is a giant shadow beast, its eyes glowing with a menacing light.")
    input()
    print("****************************\n"
            "  Desbio the Dark Beast \n"
          "****************************\n")
    input()
    print(DESBIO)
    #Prints ascii for boss
    input()
    beast_choice = input("Before either of you could move, " \
                         "Desbio strikes you both in the back, (Attack/Dodge): ")
    input()
    decrease_health()
    input()
    if beast_choice.strip().lower() == "attack":
        print("Desbio lunges at you, its claws slashing through the air.")
        input()
        decrease_health()
        #Lowers health randomly
        print(f"{COMPANION}'s health is low")
        input()
        print(f"You and {COMPANION} are both injured and need to find a way"
              "to defeat desbio before it attacks again.")
        input()
        beast_choice2 = input("You can either type 'Attack' to attack desbio or"
                              f"type 'Heal' to heal yourself and {COMPANION} (Attack/Heal): ")
        if beast_choice2.strip().lower() == "attack":
            print(f"You and {COMPANION} attack desbio with all your might,"
                  "striking it with your weapons.")
            input()
            print("Desbio roars in pain, but it is not defeated yet.")
            input()
            beast_choice3 = input("Type 'Attack' to attack desbio again or"
                                  f"type 'Heal' to heal yourself and {COMPANION} (Attack/Heal): ")
            while True:
            #These are for loops
                if beast_choice3.strip().lower() == "attack":
                    print(f"You and {COMPANION} attack desbio with all your might.")
                    input()
                    print("Desbio roars in pain, but it is not defeated yet.")
                    input()
                    print("You realize that you need to find a way to " \
                          "weaken it before you can defeat it.")
                    input()
                elif beast_choice3.strip().lower() == "heal":
                    print(f"You use a healing potion to heal yourself and {COMPANION}.")
                    increase_health(50)
                    #Increases health
                    input()
                    print(f"{COMPANION} is back in the fight!")
                    input()
                    print("You both attack desbio together, striking it with all your might.")
                    input()
                    print("Desbio roars in pain, it's scales are starting to " \
                          "crack under your combined assault.")
                    input()
                    beast_choice4 = input("Type 'Attack' to attack desbio"
                                         "again or type 'Heal' to heal"
                                         f"yourself and {COMPANION} (Attack/Heal): ")
                    if beast_choice4.strip().lower() == "attack":
                        print(f"You and {COMPANION} attack desbio's core"
                              "with all your might, striking it with your weapons.")
                        input()
                        print("Desbio roars in pain, and it crumbles to the ground, defeated.")
                        input()
                        print(f"You and {COMPANION} stand victorious, breathing"
                              "heavily from the intense battle.")
                        input()
                        print("You search the beast's remains and find a " \
                              "glowing black key that unlocks a hidden door in the dungeon.")
                        input()
                        print(f"You and {COMPANION} enter the hidden door,"
                              "hoping to find the princess inside.")
                        input()
                        print("As you step through the door, you find yourselves "
                              "in a dimly lit chamber filled with ancient artifacts.")
                        input()
                        print("In the center of the room, you see a pedestal " \
                              "with a glowing black key.")
                        input()
                        print("****************************\n"
                             "  5 Keys Achieved None left. \n"
                              "****************************\n")
                        print("You take the key and prepare to rescue the princess.")
                        input()
                        save_game()
                        dark_shield_story()
                        input()
                        chapter_12()
                        return
                        #Shows the shield upgrade story and continues
                    elif beast_choice4.strip().lower() == "heal":
                        print("Desbio lunges at you before you could " \
                              "move and summons a portal of darkness under you.")
                        death()
                        return
                    #death
                    else:
                        death()
                        return
                else:
                    print("Invalid choice. desbio attacks you again!")
                    death()
                    return
             #death due to invalid option
        elif beast_choice2.strip().lower() == "heal":
            print(f"You use a healing potion to heal yourself and {COMPANION}.")
            input()
            increase_health(50)
            print(f"{COMPANION} is back in the fight!")
            input()
            print("Desbio attacks you before you can attack again!")
            input()
            print(f"You and {COMPANION} are both injured and need to"
                  "find a way to defeat desbio before it attacks again.")
            decrease_health(50)
            input()
            print(f"{COMPANION}'s health is low")
            input()
            print("Desbio attacks you before you can attack again!")
            death()
            return
        #death
        else:
            print("Invalid choice. desbio attacks you again!")
            death()
            return
        #death due to invalid option
    elif beast_choice.strip().lower() == "dodge":
        print("You quickly dodge desbio's attack, narrowly avoiding its powerful strike.")
        input()
        print("You counterattack, striking desbio with all your might.")
        input()
        print("The beast staggers back, but it is not defeated yet."
              f"You and {COMPANION} must work together to defeat it.")
        input()
        while True:
            beast_choice5 = input("You can either type 'Attack' to"
                                  "attack desbio again or type 'Heal' to"
                                  f"heal yourself and {COMPANION} (Attack/Heal): ")
            if beast_choice5.strip().lower() == "attack":
                print(f"You and {COMPANION} attack desbio with all your might.")
                input()
                print(f"You and {COMPANION} attack desbio's core"
                      "with all your might, striking it with your weapons.")
                input()
                print("Desbio roars in pain, and it crumbles to the ground, defeated.")
                input()
                print(f"You and {COMPANION} stand victorious,"
                      "breathing heavily from the intense battle.")
                input()
                print("You search the beast's remains and find a " \
                      "glowing black key that unlocks a hidden door in the dungeon.")
                input()
                print(f"You and {COMPANION} enter the hidden door,"
                      "hoping to find the princess inside.")
                input()
                print("As you step through the door, you find yourselves "
                      "in a dimly lit chamber filled with ancient artifacts.")
                input()
                print("In the center of the room, you see a pedestal with a glowing black key.")
                input()
                print("****************************\n"
                      "  5 Keys Achieved None left. \n"
                      "****************************\n")
                input()
                save_game()
                input()
                dark_shield_story()
                input()
                chapter_12()
                return
            #Shows the shield upgrade story and continues to the next chapter
            elif beast_choice5.strip().lower() == "heal":
                print(f"You use a healing potion to heal yourself and {COMPANION}.")
                increase_health(50)
                input()
                print(f"{COMPANION} is back in the fight!")
                input()
                print("You both attack Desbio together, striking it with all your might.")
                input()
                print("Desbio roars in pain, but it's scales harden under your combined assault")
                input()
                print("Desbio attacks you before you can attack again!")
                input()
                print("Desbio charges up another burst of dark energy,"
                      f"and spews directly at you and {COMPANION}")
                input()
                death()
                break
            #Gets killed
            else:
                print("Invalid choice. Desbio attacks you again!")
                death()
                return
            #Gets killed by invalid option
    else:
        print("Invalid choice. Desbio attacks you again!")
        death()
        return
    #Gets killed by invalid option

def chapter_12():
    """
    Introduces the next chapter and the abandoned village
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_12"
    print("***************************\n"
      "Chapter 12: The Calm Before The Storm"
          "***************************\n")
    input()
    print(f"You and {COMPANION} continue down the path, now with no clue where to go...")
    input()
    print("I've heard rumours of the final"
          f"beast that captured the princess, but never the location... :{COMPANION}")
    input()
    print("We may need to camp near a village for a few days as"
          f"I try to gather some info, I'm also quite tired... :{COMPANION}")
    input()
    print(f"Wait {USERNAME}!, I see another village"
          f"over the in the horizon. Let's go! :{COMPANION}")
    input()
    print(f"You and {COMPANION} approach the village, but it looks off...")
    input()
    print(ABANDONED_VILLAGE)
    input()
    print("There are no villagers in sight, it was abandoned quite " \
          "a few months ago by the looks of it...")
    input()
    abandoned_village_choice = input("Would you like to stay or " \
                                     "leave to find another village? (Stay/Leave): ")
    if abandoned_village_choice.strip().lower() == "stay":
        print(f"Ok, {USERNAME} let's stay, we can gather info later! :{COMPANION}")
        chapter_12part2()
        return
    #Continues to the next chapter
    else:
        print(f"Ok, let's go, I'm kinda tired though... :{COMPANION}")
        input()
        print("You both travel along the path and reach a river...")
        input()
        print("You have no choice but to go back towards the village.")
        input()
        print("You arrived back at the village and sat down")
        chapter_12part2()
        input()
        return
    #Continues to next chapter and returns to the village

def chapter_12part2():
    """
    Introduces the next part of chapter 12
    """
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_12part2"
    print(f"{COMPANION} approaches one of the abandoned houses and pulls out some goods")
    input()
    print(f"You set up the fire! :{COMPANION}")
    input()
    print("You oblige and went to go get firewood nearby")
    input()
    stick1 = input("Under a tree you find a piece. Type 'One' to pick up: ")
    if stick1.strip().lower() == "one":
        print("Collected")
        #This shows the collecting stick sequence
    else:
        print("Not collected")
    stick2 = input("Under a piece of bark you find a piece. Type 'Two' to pick up: ")
    if stick2.strip().lower() == "two":
        print("Collected")
    else:
        print("Not collected")
    stick3 = input("Near the camp you find a piece. Type 'Three' to pick up: ")
    if stick3.strip().lower() == "three":
        print("Collected")
    else:
        print("Not collected")
    stick4 = input("Near a tree you find a piece. Type 'Four' to pick up: ")
    if stick4.strip().lower() == "four":
        print("Collected")
    else:
        print("Not collected")
    stick5 = input("Under a leaf you find a piece. Type 'Five' to pick up: ")
    if stick5.strip().lower() == "five":
        print("Collected all 5")
    else:
        print("Not collected")
    print("You return to the camp carrying all the wood...")
    input()
    print(f"{COMPANION} appears around a corner carrying a stack of books and yells at you")
    input()
    print(f"Come here {USERNAME} :{COMPANION}")
    input()
    print("I've analyzed the keys."
          "I believe the final creature could be dungeon somewhere underneath Fargon,"
          f"potentially underneath the capital :{COMPANION}")
    input()
    print("The capital? You ask")
    input()
    print("Yeah, according to this book,"
          f"there's a city called the capital located somewhere around here... :{COMPANION}")
    input()
    print("It's guarded by a forcefield, with 5 ancient machines guarding it")
    input()
    print("We should go find it, huh? Sounds like the princess could be located there!")
    input()
    print(f"You and {COMPANION} rest the night and leave tomorrow")
    input()
    print(f"You and {COMPANION} sleep the night")
    time.sleep(10)
    reset_health()
    chapter_13()
    #This resets the PLAYERs health to 100 and continues to the next chapter

def chapter_13():
    """
    Introduces the next chapter and the capital
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_13"
    print("***************************\n"
            "Chapter 13: The capital"
          "***************************\n")
    input()
    print(f"You and {COMPANION} set off from the abandoned village...")
    input()
    print(f"Towards where {COMPANION} thinks where the capital is...")
    input()
    print(f"You and {COMPANION} walk for days")
    time.sleep(6)
    reset_health()
    print(f"{COMPANION} looks around, 'We should be here' :{COMPANION}")
    input()
    print("What, you reply, there's nothing here")
    input()
    print("All of a sudden, the ground beneath began to shake and split open")
    input()
    print(f"You and {COMPANION} drop into the cavern below")
    input()
    decrease_health()
    input()
    print(f"You and {COMPANION} faint")
    time.sleep(10)
    print("When you wake up you notice, that COMPANION disappeared. In front of you is 5 tunnels")
    while True:
        try:
            tunnel_choice = int(input("Which tunnel would you proceed down (1-5): "))
        except ValueError:
            print("Please enter a valid number")
            continue
        match tunnel_choice:
                #This matches the PLAYERs input with a result
            case 1:
                print("You walk into the darkness of the tunnel...")
                input()
                print("You reach a dead end...")
                input()
                print("All of a sudden a skeleton attacks you from behind...")
                print(SKELETON)
                input()
                death()
                break
            case 2:
                print("You walk into the darkness of the tunnel...")
                input()
                print("In the end, you reach a fountain...")
                input()
                print("Your deadly thirsty and drank from the fountain...")
                input()
                print("The fountain water was poisoned.")
                death()
                break
            case 3:
                print("You walk into the darkness of the tunnel...")
                input()
                print(f"You notice, a shadow up ahead, it could be {COMPANION}...")
                input()
                print("You run towards the shadow...")
                input()
                print("You walk right past the shadow...")
                input()
                print(f"You arrive back at the village, alone, with no {COMPANION} in sight...")
                input()
                print("You died of loneliness and despair")
                input()
                death()
                break
            case 4:
                print("You walk into the darkness of the tunnel...")
                input()
                print(f"You notice a shadow up ahead, it could be {COMPANION}...")
                input()
                print(f"Hey, come {USERNAME}! :{COMPANION}")
                input()
                print("You run towards the shadow...")
                input()
                print(f"You arrive at {COMPANION} and hug them tightly")
                input()
                print(f"{COMPANION} says, 'I thought I lost you!'")
                input()
                print("You realise that there was a blue misty wall at the " \
                      "end of the tunnel blocking your way further...")
                input()
                print(f"You and {COMPANION} then spot another tunnel to the"
                      "right of the blue wall...")
                input()
                print(f"You and {COMPANION} walk down the tunnel, hoping to find to the capital")
                input()
                chapter_14()
                break
            #This goes to the next chapter
            case 5:
                print("You walk into the darkness of the tunnel...")
                input()
                print("You spot  a faint light in the distance...")
                input()
                print("You walk towards the light...")
                input()
                print("You arrive at a small campfire, with a note next to it...")
                input()
                print("The note reads: 'Beware of the final beast, " \
                      "it lurks in the shadows of the capital.'")
                input()
                print("You take the note and continue down the tunnel...")
                input()
                print("You arrive at a dead end, with no way out...")
                input()
                print("You sit down and wait for help...")
                input()
                print("After a few hours, you hear a voice calling your name...")
                input()
                print(f"It sounds like {COMPANION}, yet it doesn't!")
                input()
                print("You stand up and walk towards the voice...")
                input()
                print("You arrive at a small clearing, " \
                      "with a shadowy figure standing in the middle.")
                input()
                print("The figure is cloaked in darkness, its eyes glowing with a menacing light.")
                input()
                print("****************************\n"
                      "  The Shadowy Figure \n"
                      "****************************\n")
                input()
                print(MYSTERIOUS_CHARACTER)
                input()
                print("You have come far, but you will not find the princess here. " \
                      ":Mysterious Figure")
                input()
                print(f"You ask the figure where the princess and {COMPANION} is,"
                      "but it only laughs.")
                input()
                print("The figure lunges at you, its claws slashing through the air.")
                input()
                print("You try to dodge the attack, but the figure is too fast.")
                input()
                print(f"You've came far, yet this is where it ends for you, {USERNAME}.")
                input()
                print("The figure strikes you down, and you fall to the ground, defeated.")
                input()
                print("You hear the figure laugh as it disappears into the shadows.")
                input()
                print("This creature was not the final beast, " \
                      "but a mere shadow of what is to come.")
                input()
                death()
                break
            #This kills the PLAYER
            case _:
                print("Enter a valid number")
                return
            #This loops until the PLAYER enters a valid number

def chapter_14():
    """
    Introduces the first machine and the first guardian fight
    """
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_14"
    print("***************************\n"
          "Chapter 14: The First Machine\n"
          "***************************\n")
    input()
    print(f"You and {COMPANION} arrive at the first machine,"
          "a massive structure made of stone and metal.")
    input()
    print("The machine is covered in strange symbols and runes, "
          "and it seems to be powered by some kind of dark energy.")
    input()
    print(f"This must be one of the machines that guard the capital. :{COMPANION}")
    input()
    print("You nod in agreement, determined to find a way to disable the machine.")
    input()
    print("As you approach the machine, you notice a small" \
          "panel on the side with a glowing red button.")
    input()
    print(f"We need to find a way to activate this button. :{COMPANION}")
    input()
    print("You search the area around the machine and find a small lever hidden behind some rocks.")
    input()
    print("You pull the lever, and the machine comes to life, its gears " \
          "grinding and whirring as it powers up.")
    input()
    print("The glowing red button on the panel lights up, and you press it.")
    input()
    print("The machine shudders and shakes, and you can feel the ground beneath you tremble.")
    input()
    print("Suddenly, a massive door opens in the side of the machine, " \
          "revealing a dark chamber inside.")
    input()
    print(f"We need to go inside and see what we can find. :{COMPANION}")
    input()
    print(f"You and {COMPANION} enter the chamber, weapons drawn, ready for whatever lies ahead.")
    input()
    print("Inside the chamber, you find a series of strange machines "
          "and devices, all connected to a button on a pedestal in the center of the room.")
    input()
    print("You approach the pedestal and see that the button is glowing with a dark energy.")
    input()
    print("All of a sudden, you feel a strange urge " \
          "to press the button, as if it is calling to you.")
    input()
    print(f"We need to be careful. This could be a tra.. :{COMPANION}")
    input()
    print(f"But before {COMPANION} can finish their sentence, you press the button.")
    input()
    print("The machine shudders and shakes, and you can feel the ground beneath you tremble.")
    input()
    print("Suddenly, the machines in the room all spring to life, " \
          "their gears grinding and whirring as they power up.")
    input()
    print("You hear a loud rumbling noise, and the machines begin to open a trapdoor in the floor.")
    input()
    print(f"You and {COMPANION} look at each other, unsure of what to do next.")
    input()
    print("*****************************\n"
           "     The First guardian \n"
          "*****************************\n")
    input()
    guardian1()
#This goes to the first guardian fight

def guardian1():
    """
    Introduces the first guardian fight
    """
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "guardian1"
    print("Suddenly, a massive mechanical guardian emerges from the trapdoor, " \
          "its eyes glowing with a menacing light.")
    input()
    print("The guardian is a towering figure made of metal and stone, " \
          "its body covered in intricate designs and runes.")
    input()
    print("It raises its massive fists, ready to attack.")
    input()
    print(f"You and {COMPANION} prepare for battle, your weapons drawn and ready to fight.")
    input()
    print("The guardian lunges at you, its fists swinging through the air.")
    input()
    print("You dodge the attack and strike back, hitting the guardian in the side.")
    input()
    print("The guardian roars in pain, but it is not defeated yet.")
    input()
    guardian_choice = input("Do you want to attack the guardian again or try " \
                            "to find a way to disable the machines? (Attack/Disable): ")
    if guardian_choice.strip().lower() == "attack":
        print(f"You and {COMPANION} attack the guardian with all your might,"
              "striking it with your weapons.")
        input()
        print("The guardian roars in pain, but it is not defeated yet.")
        input()
        print("You realize that you need to find a way to disable " \
              "the machines before you can defeat the guardian.")
        input()
        disable_choice = input("Do you want to try to disable the machines "
                               "or keep attacking the guardian? (Disable/Attack): ")
        if disable_choice.strip().lower() == "disable":
            print(f"You and {COMPANION} search the room for a way to disable the machines.")
            input()
            print("You find a control panel on the wall with a series of buttons and switches.")
            input()
            print("You quickly figure out how to disable the machines, "
                  "and they all shut down, leaving the guardian vulnerable.")
            input()
            print(f"You and {COMPANION} attack the guardian one last time,"
                  "striking it down and defeating it.")
            input()
            print("You search the guardian's remains and find a glowing red " \
                  "key that unlocks a hidden door in the machine.")
            input()
            print(f"You and {COMPANION} enter the hidden door,"
                  "hoping to find more clues about the final beast.")
            input()
            chapter_15()
        #This goes to chapter 15
        elif disable_choice.strip().lower() == "attack":
            print(f"You and {COMPANION} keep attacking the guardian, but it is too strong.")
            input()
            print("The guardian strikes you down, and you fall to the ground, defeated.")
            input()
            death()
            return
        #death
        else:
            print("The guardian doesn't hesitate to attack back")
            death()
        #This kills the PLAYER due to invalid response
    elif guardian_choice.strip().lower() == "disable":
        print(f"You and {COMPANION} search the room for a way to disable the machines.")
        input()
        print("You find a control panel on the wall with a series of buttons and switches.")
        input()
        print("You quickly figure out how to disable the machines, "
              "and they all shut down, leaving the guardian vulnerable.")
        input()
        print(f"You and {COMPANION} attack the guardian one last time,"
              "striking it down and defeating it.")
        input()
        print("You search the guardian's remains and find a glowing red key " \
              "that unlocks a hidden door in the machine.")
        input()
        print(f"You and {COMPANION} enter the hidden door, hoping to"
              "find more clues about the final beast.")
        input()
        chapter_15()
    #This goes to the nest chapter
    else:
        print("The guardian lumbers over towards you and crushes you")
        death()

def chapter_15():
    """
    Introduces the second machine and the second guardian fight
    """
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_15"
    print("***************************\n"
          "Chapter 15: The Second Machine\n"
          "***************************\n")
    input()
    print(f"You and {COMPANION} enter the second machine,"
          "a massive structure filled with gears and machinery.")
    input()
    print("The air is thick with the smell of rusty metal, "
          "and you can hear the sound of machinery whirring to life.")
    input()
    print("We need to find a way to"
          f"shut down this machine before it activates. :{COMPANION}")
    input()
    print("You nod in agreement, determined to stop the machine and find the final beast.")
    input()
    print("As you explore the machine, you come across a series of control panels and levers.")
    input()
    print("You quickly figure out how to disable the machine, and it begins to shut down.")
    input()
    print("But before you can celebrate, another massive mechanical " \
          "guardian emerges from the shadows, its eyes glowing with a menacing light.")
    input()
    print("The guardian is a towering figure made of metal and stone, " \
          "its body covered in intricate designs and runes.")
    input()
    print("It raises its massive fists, ready to attack.")
    input()
    print("****************************\n"
          "  The Second guardian \n"
          "****************************\n")
    input()
    guardian2()
#This goes to the next stage of the battle

def guardian2():
    """
    Introduces the second guardian fight
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "guardian2"
    print("The guardian lunges at you, its fists swinging through the air.")
    input()
    print("You dodge the attack and strike back, hitting the guardian in the side.")
    input()
    print("The guardian roars in pain, but it is not defeated yet.")
    input()
    guardian_choice = input("Do you want to attack the guardian again or try " \
                            "to find a way to disable the machines? (Attack/Disable): ")
    if guardian_choice.strip().lower() == "attack":
        print(f"You and {COMPANION} attack the guardian with all your might,"
              "striking it with your weapons.")
        input()
        print("The guardian roars in pain, but it is not defeated yet.")
        input()
        print("You realize that you need to find a way to disable the " \
              "machines before you can defeat the guardian.")
        input()
        disable_choice = input("Do you want to try to disable the machines "
                               "or keep attacking the guardian? (Disable/Attack): ")
        if disable_choice.strip().lower() == "disable":
            print(f"You and {COMPANION} search the room for a way to disable the machines.")
            input()
            print("You find a control panel on the wall with a series of buttons and switches.")
            input()
            print("You quickly figure out how to disable the machines, "
                  "and they all shut down, leaving the guardian vulnerable.")
            input()
            print(f"You and {COMPANION} attack the guardian one last time,"
                  "striking it down and defeating it.")
            input()
            print("You search the guardian's remains and find a glowing " \
                  "blue key that unlocks a hidden door in the machine.")
            input()
            print(f"You and {COMPANION} enter the hidden door,"
                  "hoping to find more clues about the final beast.")
            input()
            final_machine()
        #Goes to next chapter
        elif disable_choice.strip().lower() == "attack":
            print(f"You and {COMPANION} keep attacking the guardian, but it is too strong.")
            input()
            print("The guardian strikes you down, and you fall to the ground, defeated.")
            input()
            death()
        #kills the PLAYER
        else:
            print("The guardian suddenly stops moving")
            input()
            print(f"You and {COMPANION} stare bewildered")
            input()
            print("Suddenly, the guardian explodes")
            input()
            print("All those years being inactive and inside this humid room " \
                  "must have rusted something")
            death()
            return
    elif guardian_choice.strip().lower() == "disable":
        print(f"You and {COMPANION} search the room for a way to disable the machines.")
        input()
        print("You find a control panel on the wall with a series of buttons and switches.")
        input()
        print("You quickly figure out how to disable the machines, "
              "and they all shut down, leaving the guardian vulnerable.")
        input()
        print(f"You and {COMPANION} attack the guardian one last time,"
              "striking it down and defeating it.")
        input()
        print("You search the guardian's remains and find a glowing " \
              "blue key that unlocks a hidden door in the machine.")
        input()
        print(f"You and {COMPANION} enter the hidden door,"
              "hoping to find more clues about the final beast.")
        input()
        final_machine()
    else:
        print("The guardian swings it huge arms at you")
        death()
        return
    #Goes to next chapter

def final_machine():
    """
    Introduces the final machine
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "final_machine"
    print("***************************\n"
          "Chapter 16: The Final Machine\n"
          "***************************\n")
    input()
    print(f"You and {COMPANION} enter the final machine,"
          "a massive structure filled with gears and machinery.")
    input()
    print("The air is thick with the smell of rusty metal, "
          "and you can hear the sound of machinery whirring to life.")
    input()
    print(f"This is it. The final machine that guards the capital. :{COMPANION}")
    input()
    print("You nod in agreement, determined to find a way to " \
          "shut down the machine and rescue the princess.")
    input()
    print("As you explore the machine, you come across a series of control panels and levers.")
    input()
    print("You quickly figure out how to disable the machine, and it begins to shut down.")
    input()
    print("You hear a loud rumbling noise, and the machines" \
          " begin to shut down the forcefield that surrounds the capital.")
    input()
    print(f"With the forcefield down, you and {COMPANION} rush out"
          "of the machine rooms and make your way to the heart of the capital.")
    chapter_16()
#This goes to the next chapter after disabling the forcefield

def chapter_16():
    """
    Introduces the final chapter and the final boss fight
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_16"
    print("***************************\n"
          "Chapter 16: The Final Showdown\n"
          "***************************\n")
    input()
    print(f"You and {COMPANION} enter the capital,"
          "a grand city filled with towering buildings and bustling streets.")
    input()
    print(NECRON)
    input()
    print("But something is off. The streets are eerily quiet, "
          "and you can feel a dark presence lurking in the shadows.")
    input()
    print(f"We need to find the final beast and rescue the princess. :{COMPANION}")
    input()
    print("You nod in agreement, determined to find the final beast and rescue the princess.")
    input()
    print("The grand architecture of the capital is breathtaking, " \
          "but the atmosphere is heavy with dread.")
    input()
    print("Gothic style buildings loom overhead, their windows dark and foreboding.")
    input()
    print("As you walk through the empty streets, you notice strange symbols " \
          "etched into the walls.")
    input()
    print("These symbols seem to pulse with a dark energy, "
          "and you can feel their power as you pass by.")
    input()
    print(f"{COMPANION} says, 'These symbols must be connected to the final beast.'")
    input()
    print(f"You and {COMPANION} continue to explore the capital,"
          "searching for any clues that might lead you to the final beast.")
    input()
    print("As you venture deeper into the capital, " \
          "you come across a large underground chamber filled with darkness " \
          "with a few crates inside.")
    input()
    print("In the center of the chamber, you see a pedestal with a glowing purple key.")
    input()
    print("But before you can approach the pedestal," \
          "a massive shadowy figure emerges from the darkness.")
    input()
    print("The figure is a giant shadow beast, its eyes glowing with a menacing light.")
    input()
    print("****************************\n"
    "   necron The Beast of Eternal Doom \n"
          "****************************\n")
    input()
    print(NECRON)
    input()
    save_game()
    necron_fight()
#This starts the boss fight

def necron_fight():
    """
    Introduces the first part of the necron fight
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "Necron_fight"
    print("The beast lunges at you, its claws slashing through the air.")
    input()
    print("You dodge the attack and strike back, hitting the beast in the side.")
    input()
    print("Necron roars in pain, but it is not defeated yet.")
    input()
    necron_choice = input("Do you want to attack the beast again or heal? (Attack/Heal): ")
    if necron_choice.strip().lower() == "attack":
        print(f"You and {COMPANION} attack the beast with all your might,"
              "striking it with your weapons.")
        input()
        print("The beast roars in pain, but it is not defeated yet.")
        input()
        print("Necron is too strong, and you realize that you need to find " \
              "a way to disable the machines before you can defeat it.")
        input()
        disable_choice = input("Do you want to try to disable the machines "
                               "or keep attacking the beast? (Heal/Attack): ")
        if disable_choice.strip().lower() == "heal":
            print(f"You and {COMPANION} search the cavern for a way to heal yourselves.")
            input()
            print("You find a stash of healing potions and quickly use them " \
                  "to restore your health.")
            input()
            print("With your health restored, you feel ready to take on the beast again.")
            input()
            necron_fight2()
        #Goes to the second part of the fight
        elif disable_choice.strip().lower() == "attack":
            print(f"You and {COMPANION} keep attacking the beast, but it is too strong.")
            input()
            print("The beast strikes you down, and you fall to the ground, defeated.")
            input()
            death()
        #Death
        else:
            print("Invalid choice. You continue to attack the beast without healing.")
            input()
            necron_fight2()
        #Goes to the second part of the fight without heal
    elif necron_choice.strip().lower() == "heal":
        print(f"You and {COMPANION} search the cavern for a way to heal yourselves.")
        input()
        print("You find a stash of healing potions and quickly use them to restore your health.")
        input()
        print("With your health restored, you feel ready to take on the beast again.")
        input()
        necron_fight2()
    #Goees to second part of the fight
    else:
        print("Invalid choice. necron casts a dark spell, "
              "and you feel your strength draining away.")
        input()
        death()
        return
    #death

def necron_fight2():
    """
    Introduces the second sequence of the necron fight
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "Necron_fight2"
    print("AHHHHHH, LIGHT WILL NEVER COME OVER THIS WORLD, " \
          "YOU CAN'T STOP ME YOU PUNY LITTLE INSECTS! necron yells")
    necron_choice2 = input("Do you want to attack the beast again or heal? (Attack/Heal): ")
    if necron_choice2.strip().lower() == "attack":
        print(f"You and {COMPANION} attack the beast with all your might,"
              "striking it with your weapons.")
        input()
        print("The beast roars in pain, but it is not defeated yet.")
        input()
        print("Necron is too strong, and you realize that there are machines " \
              "surrounding the room healing necron, you need to find a way to " \
              "disable the machines before you can defeat it.")
        input()
        disable_choice2 = input("Do you want to try to disable the machines "
                                "or keep attacking the beast? (Disable/Attack): ")
        if disable_choice2.strip().lower() == "disable":
            print(f"You and {COMPANION} search the cavern for a way to disable the machines.")
            input()
            print("You find a control panel on the wall with a series of " \
                  "buttons and switches and a book full of unknown letters.")
            input()
            print("You quickly flip through the book and find a passage " \
                  "that seems to describe the machines.")
            input()
            print("With this knowledge, you feel ready to take on the machines.")
            input()
            machines1()
        #Goes to next part
        elif disable_choice2.strip().lower() == "attack":
            print(f"You and {COMPANION} keep attacking the beast, but it is too strong.")
            input()
            print("The beast strikes you down, and you fall to the ground, defeated.")
            input()
            death()
            return
        #death
        else:
            print("Necron suddenly slams into the cavern causing it to"
                  f"collapse on top of you and {COMPANION}")
            death()
            return
    elif necron_choice2.strip().lower() == "heal":
        print(f"You and {COMPANION} search the cavern for a way to heal yourselves.")
        input()
        print("You find a stash of healing potions and quickly use them to restore your health.")
        input()
        print("With your health restored, you feel ready to take on the beast again.")
        input()
        necron_fight3()
    #Starts next sequence of the boss fight
    else:
        print(f"Necron summons a stack of playing cards on top of you and {COMPANION},"
              "crushing you both")
        death()
        return

def necron_fight3():
    """
    Introduces the third sequence of the necron fight
    """
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "Necron_fight3"
    print("Necron roars in anger, its eyes glowing with a menacing light.")
    input()
    print("The beast lunges at you, its claws slashing through the air.")
    input()
    print("You dodge the attack and strike back, hitting the beast in the side.")
    input()
    print("Necron roars in pain, but it is not defeated yet.")
    input()
    necron_choice3 = input("Do you want to attack the beast again or " \
                           "destroy the machines? (Attack/Destroy): ")
    if necron_choice3.strip().lower() == "attack":
        print(f"You and {COMPANION} attack the beast with all your might,"
              "striking it with your weapons.")
        input()
        print("The beast roars in pain, but it is not defeated yet.")
        input()
        print("Necron is too strong, and you realize that you need to find a " \
              "way to destroy the machines before you can defeat it.")
        input()
        destroy_choice = input("Do you want to try to destroy the machines "
                               "or keep attacking the beast? (Destroy/Attack): ")
        if destroy_choice.strip().lower() == "destroy":
            print(f"You and {COMPANION} search the cavern for a way to destroy the machines.")
            input()
            print("You find a control panel on the wall with a series of " \
                  "buttons and switches and a book full of unknown letters.")
            input()
            print("You quickly flip through the book and find a passage " \
                  "that seems to describe the machines.")
            input()
            print("With this knowledge, you feel ready to take on the machines.")
            input()
            machines1()
        elif destroy_choice.strip().lower() == "attack":
            print(f"You and {COMPANION} keep attacking the beast, but it is too strong.")
            input()
            print("The beast strikes you down, and you fall to the ground, defeated.")
            input()
            death()
        #Gets killed
        else:
            print(f"You and {COMPANION} look in dread as necron summons a hoard of goblins")
            input()
            print(f"The disoriented goblins start swarming you and {COMPANION}")
            input()
            death()
            return
    elif necron_choice3.strip().lower() == "destroy":
        print("You search the cavern for a way to destroy the machines"
              f"while {COMPANION} distracts Necrom.")
        input()
        print("You find a control panel on the wall with a series of buttons "
              "and switches and a book full of unknown letters.")
        input()
        print("You quickly flip through the book and find a passage " \
              "that seems to describe the machines.")
        input()
        print("With this knowledge, you feel ready to take on the machines.")
        input()
        machines1()
    #Goes to the next chapter


def machines1():
    """
    Introduces the first machine and the first destroy sequence
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "machines1"
    print("You spot the first machine, a massive structure made of stone and metal.")
    input()
    destroy1 = input("To destroy it type (XYSDFBA): ")
    if destroy1.strip().lower() == "xysdfba":
        print("You successfully destroy the first machine, and it crumbles to the ground.")
        input()
        print("You search the machine's remains and find a glowing " \
              "red key that unlocks a hidden door in the capital.")
        input()
        print(f"You and {COMPANION} enter the hidden door,"
              "hoping to find more clues about the final beast.")
        input()
        machines2()
    #Goes to next chapter
    else:
        print("You fail to destroy the first machine, and it remains intact.")
        input()
        print("You realize that you need to find a way to disable the " \
              "machine before you can proceed.")
        input()
        machines1()
    #Repeats

def machines2():
    """
    Introduces the second machine and the second destroy sequence
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "machines2"
    print("You spot the second machine, a massive structure made of sharpened serpent scales.")
    input()
    destroy2 = input("To destroy it type (DNQEJJ): ")
    if destroy2.strip().lower() == "dnqejj":
        print("You successfully destroy the second machine, and it crumbles to the ground.")
        input()
        print("You search the machine's remains and find a glowing " \
              "red key that unlocks a hidden door in the capital.")
        input()
        print(f"You and {COMPANION} enter the hidden door,"
              "hoping to find more clues about the final beast.")
        input()
        machines3()
    #Goes to next chapter
    else:
        print("You fail to destroy the second machine, and it remains intact.")
        input()
        print("You realize that you need to find a way to disable " \
              "the machine before you can proceed.")
        input()
        machines2()
    #Repeats

def machines3():
    """
    Introduces the third machine and the third destroy sequence
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "machines3"
    print("You spot the third machine, a massive structure made of solidified lava.")
    input()
    destroy3 = input("To destroy it type (FNJREWNFJ): ")
    if destroy3.strip().lower() == "fnjrewnfj":
        print("You successfully destroy the third machine, and it crumbles to the ground.")
        input()
        print("You search the machine's remains and find a glowing " \
              "red key that unlocks a hidden door in the capital.")
        input()
        print(f"You and {COMPANION} enter the hidden door,"
              "hoping to find more clues about the final beast.")
        input()
        machines4()
    #Goes to next chapter
    else:
        print("You fail to destroy the third machine, and it remains intact.")
        input()
        print("You realize that you need to find a way to disable " \
              "the machine before you can proceed.")
        input()
        machines3()
    #Repeats

def machines4():
    """
    Introduces the fourth machine and the fourth destroy sequence
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "machines4"
    print("You spot the fourth machine, a massive structure made of pure packed ice.")
    input()
    destroy4 = input("To destroy it type (FNJQNRE): ")
    if destroy4.strip().lower() == "fnjqnre":
        print("You successfully destroy the fourth machine, and it crumbles to the ground.")
        input()
        print("You search the machine's remains and find a glowing " \
              "red key that unlocks a hidden door in the capital.")
        input()
        print(f"You and {COMPANION} enter the hidden door,"
              "hoping to find more clues about the final beast.")
        input()
        machines5()
    #Goes to next chapter
    else:
        print("You fail to destroy the fourth machine, and it remains intact.")
        input()
        print("You realize that you need to find a way to disable " \
              "the machine before you can proceed.")
        input()
        machines4()
    #Repeats

def machines5():
    """
    Introduces the fifth machine and the fifth destroy sequence
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "machines5"
    print("You spot the final machine, a massive structure made of pure refined darkness.")
    input()
    destroy5 = input("To destroy it type (JDEIJDU): ")
    if destroy5.strip().lower() == "jdeijdu":
        print("You successfully destroy the fifth machine, and it crumbles to the ground.")
        input()
        print("Just in time, you turn around and see necron, the final beast, charging at you.")
        input()
        print(f"{COMPANION} is nowhere to be seen,"
              "and you realize that you are alone in this fight.")
        input()
        necron_fight4()
    #Goes to next part of the fight
    else:
        print("You fail to destroy the fifth machine, and it remains intact.")
        input()
        print("You realize that you need to find a way to disable " \
              "the machine before you can proceed.")
        input()
        machines5()
    #Repeats

def necron_fight4():
    """
    Introduces the final sequence of the necron fight
    """
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "Necron_fight4"
    print("Necron roars in anger, its eyes glowing with a darker menacing light.")
    input()
    print("Necron shrieks another battle cry, "
          "and transforms into it's second form, a massive shadowy dragon.")
    input()
    print("*************************************\n"
"      necronom The Final Bringer of Eternal Darkness \n"
          "************************************\n")
    input()
    print(NECRON_SECOND_FORM)
    input()
    print("The dragon lunges at you, its claws slashing through the air.")
    input()
    print("You dodge the attack and strike back, hitting the dragon in the side.")
    input()
    print("Necronom roars in pain, but it is not defeated yet.")
    input()
    dragon_choice = input("Do you want to attack the dragon again or heal? (Attack/Heal): ")
    #Saves input as dragon_choice
    if dragon_choice.strip().lower() == "attack":
        print(f"You and {COMPANION} attack the dragon with all your might,"
              "striking it with your weapons.")
        input()
        print("The dragon roars in pain, but it is not defeated yet.")
        input()
        print("Necronom is too strong, and yet you perservere through the pain "
              "and realize that inside one of the crates, is a book full of spells.")
        input()
        disable_choice = input("Do you want to try to cast a spell or" \
                               "keep attacking the dragon? (Cast/Attack): ")
        if disable_choice.strip().lower() == "cast":
            print("You grab the book and quickly flip through the pages, " \
                  "searching for a spell that can help you defeat the dragon.")
            input()
            print(DARK_BOOK)
            input()
            print("You find a spell that seems to describe the dragon, "
                  "and you quickly memorize it.")
            input()
            print("Nazma incus draconis! you chant, and a burst of light erupts from your hands.")
            input()
            print("The dragon roars in pain, and you can see its " \
                  "scales begin to crack and crumble.")
            input()
            print("AHHHHHHHHHHHHHHHHHHHHHH, NOOOOOOOOOOOO! necronom screams  as it " \
                  "begins to disintegrate.")
            input()
            print("THIS WILL NOT BE THE END, THE PRINCESS IS NOT WHO SHE SEEMS, " \
                  "YOU WILL NEVER ESCAPE THIS PLACE ALIVE! necronom yells as " \
                  "it fades into the shadows.")
            input()
            print("You search the dragon's remains and find a glowing " \
                  "purple key that unlocks a hidden door in the chamber.")
            input()
            print(f"You and {COMPANION} enter the hidden door,"
                  "hoping to find more clues about the final beast.")
            input()
            companion_fight()
        #Continues to next chapter
        elif disable_choice.strip().lower() == "attack":
            print(f"You and {COMPANION} keep attacking the dragon, but it is too strong.")
            input()
            print("The dragon strikes you down, and you fall to the ground, defeated.")
            input()
            death()
        #death
        else:
            print("Invalid choice. The dragon strikes you down, "
                  "and you fall to the ground, defeated.")
            input()
            death()
        #death due to invalid response
    elif dragon_choice.strip().lower() == "heal":
        print("Necronom charges into you and picks you up high before dropping you")
        death()
    else:
        print("Necronom strikes you and COMPANION")
        death()


def companion_fight():
    """
    Introduces the companion fight
    """
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "companion_fight"
    print("As you enter the hidden door, you find yourself in a " \
          "large chamber filled with darkness.")
    input()
    print("In the center of the chamber, you see a pedestal with a glowing purple key.")
    input()
    print("But before you can approach the pedestal, you hear a voice calling your name.")
    input()
    print(f"You turn around to look at {COMPANION} but he looks off")
    input()
    print("Their eyes are glowing with a dark energy.")
    input()
    print(f"{COMPANION} says, 'You have come far, but you will not find the princess here.'")
    input()
    print("The voice is distorted and twisted,"
          f"and you can feel a dark presence emanating from {COMPANION}.")
    input()
    print("****************************\n"
            "  Corrupted COMPANION \n"
          "****************************\n")
    input()
    print(f"You realize that {COMPANION} has been corrupted by"
          "the dark energy of necron, and you must fight them to save the princess.")
    input()
    companion_choice = input(f"Do you want to attack {COMPANION} or"
                             "try to reason with them? (Attack/Reason): ")
    if companion_choice.strip().lower() == "reason":
        print(f"You try to reason with {COMPANION},"
              "but they are too far gone.")
        input()
        print(f"The corrupted {COMPANION} is strong,"
              "but you are determined to save them.")
        input()
        print(f"Too late, the corrupted {COMPANION} lunges at you,"
              "their claws slashing through the air.")
        input()
        print(f" {COMPANION} manages to strike you down,"
              "and you fall to the ground, defeated.")
        input()
        print(f"I'm sorry, {USERNAME}, but I cannot let you find the princess,"
              f"their voice distorted and twisted. :{COMPANION}")
        input()
        print(f"{COMPANION} leaves you lying on the ground, defeated,"
              "and walks away into the darkness.")
        input()
        print(f"You've made it far, but this is where it ends for you. :{COMPANION}")
        input()
        print(f"You hear the corrupted {COMPANION}"
              "laugh as they disappear into the shadows.")
        death()
        return
    elif companion_choice.strip().lower() == "attack":
        print(f"You lunge at {COMPANION},"
              "your eyes filled with tears yet your heart filled with determination.")
        input()
        print(f"{COMPANION} tries to dodge your attack,"
              "but you manage to hit them in the side.")
        input()
        print(f"Wait, {USERNAME}, I can still be saved! "
              f"their voice filled with pain. :{COMPANION}")
        input()
        companion_choice2 = input(f"Would you like to continue attacking {COMPANION}"
                                  "or try to save them? (Attack/Save): ")
        input()
        if companion_choice2.strip().lower() == "save":
            print("Fine, you reply")
            input()
            print(f"Thank you, {USERNAME}, I knew you would come to save me!"
                  f"their voice filled with hope. :{COMPANION}")
            input()
            print(f"You help {COMPANION} to their feet,"
                  "and they look at you with gratitude in their eyes.")
            input()
            print(f"'Come let's go, we need to get out of here', you say to {COMPANION}")
            input()
            print("We need to go find the princ...")
            input()
            print(f"{COMPANION} striked you in the bag,"
                  "their eyes glowing with a dark energy once again.")
            input()
            print("You really thought I was going to let you save me?"
                  f"{COMPANION} says, their voice distorted and twisted.")
            input()
            print(f"Bye bye, {USERNAME}, I hope you enjoy your"
                  f"stay in the darkness, {COMPANION} says with a sinister laugh.")
            death()
            return
        elif companion_choice2.strip().lower() == "attack":
            print(f"You keep attacking {COMPANION},"
                  "determined to defeat them and save the princess.")
            input()
            print(f"The corrupted {COMPANION} fights back with all their might,"
                  "but you are relentless in your attack.")
            input()
            print("Finally, after a long and grueling battle,"
                  f"{COMPANION} surrenders.")
            input()
            print(f"Fine, I'm sorry, {USERNAME}, I didn't mean to hurt you,"
                  f"their voice filled with pain. :{COMPANION}")
            input()
            print("No, you replied, you were corrupted by the dark energy of necron, "
                   "and you must be stopped.")
            input()
            print(f"You hoist your sword towards {COMPANION},"
                  "ready to strike the final blow.")
            input()
            print("But before you can strike, you remember"
                  f"all the fond memories you had with {COMPANION}.")
            input()
            print("You remember the times you laughed together, " \
                  "the times you fought side by side, all the dungeons you faced together.")
            input()
            print(f"You realize that you cannot bring yourself to kill {COMPANION},"
                  "even if they corrupted, but yet he could still hurt you.")
            input()
            companion_choice3 = input(f"Do you want to spare {COMPANION} or"
                                      "finish them off? (Spare/Finish): ")
            if companion_choice3.strip().lower() == "spare":
                print("You lower your sword, tears streaming down your face.")
                input()
                print(f"I can't do it, {COMPANION},"
                      "I can't do it, you say, your voice filled with emotion.")
                input()
                print(f"{COMPANION} looks at you with gratitude in their eyes,"
                      "and they fall to their knees, their eyes filled with tears.")
                input()
                print(f"Thank you, {USERNAME}, I knew you would come to save me,"
                      f"their voice filled with hope. :{COMPANION}")
                input()
                print("I can't kill you, even if you are corrupted, " \
                      "you say, your voice filled with emotion.")
                input()
                print("The book which you used to kill necronon, starts to pulse")
                input()
                print("All of a sudden, it opens and frees from your " \
                      "clutches and begins to float in the air.")
                input()
                print(f"{COMPANION} begins to float in the air alongside the book")
                input()
                print(f"Suddenly, lightning strikes {COMPANION}"
                      "and they collapse to the ground, weak but you feel " \
                      "that the dark energy is gone.")
                chapter_17()
            elif companion_choice3.strip().lower() == "finish":
                print(f"You raise your sword and deliver the final blow to {COMPANION},"
                      "ending their corrupted existence.")
                input()
                print(f"With their last breath, {COMPANION} looks at you"
                      "with a mix of gratitude and sorrow.")
                input()
                print(f"Thank you for freeing me, {USERNAME}, {COMPANION}"
                      "whispers before fading away.")
                input()
                print("You look down at the remains of your once beloved Companion, your " \
                       "heart heavy with sorrow.")
                input()
                print("You begin to feel regret for what you have done.")
                input()
                print("You feel an awful sensation in your chest, "
                      "and you realize that you have lost a part of yourself.")
                input()
                print("You faint and collapse")
                input()
                print("You died, due to loneliness and sorrow")
                death()
                return
            else:
                print(f"Invalid choice. The corrupted {COMPANION} strikes you down,"
                      "and you fall to the ground, defeated.")
                input()
                death()
        else:
            print(f"Invalid choice. The corrupted {COMPANION} strikes you down,"
                  "and you fall to the ground, defeated.")
            input()
            death()
    else:
        print(f"Invalid choice. The corrupted {COMPANION} strikes you down,"
              "and you fall to the ground, defeated.")
        input()
        death()

def chapter_17():
    """
    Introduces the aftermath of the necron fight and the companion's recovery
    """
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_17"
    print("***************************\n"
            "Chapter 17: The Princess?\n"
          "***************************\n")
    input()
    print(f"Uhhh, where am I?? {COMPANION} says, as they slowly regain consciousness. :{COMPANION}")
    input()
    print(f"What happened?, {COMPANION} asks, looking around the abandoned house.")
    input()
    print(f"You explain to {COMPANION} that you defeated necron and"
          "saved them from the dark energy that corrupted them.")
    input()
    print(f"{COMPANION} looks at you with gratitude in their eyes, and"
          "they fall to their knees, their eyes filled with tears.")
    input()
    print(f"Thank you, {USERNAME}, I knew you would come to save me,"
          f" their voice filled with hope. :{COMPANION}")
    input()
    print(f"You help {COMPANION} to their feet, and they look at you with gratitude in their eyes.")
    input()
    print(f"'Come let's go, we need to find the princess', you say to {COMPANION}")
    input()
    print(f"You and {COMPANION} leave the abandoned house and"
          "make your way to the heart of the capital.")
    input()
    print("As you walk through the empty streets, " \
          "you once again notice the strange symbols etched into the walls " \
          "but now they've seem to be faded away.")
    input()
    print(f"I want to get out of here, their voice filled with determination :{COMPANION}")
    input()
    print("You nod in agreement, determined to find the princess and escape the capital.")
    input()
    print("At the center of the capital, lies the princess's castle,"
          f" 'It's most likely she's trapped in there. :{COMPANION}")
    input()
    print(f"You and {COMPANION} make your way to the castle,"
          "hoping to find the princess and escape the capital.")
    chapter_18()

def chapter_18():
    """
    Introduces the castle and the corrupted princess
    """
    #Docstring to describe the chapter
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_18"
    print("***************************\n"
          "Chapter 18: The Castle\n"
          "***************************\n")
    input()
    print(f"You and {COMPANION} arrive at the castle,"
          "a grand gothic structure filled with towering walls and ornate decorations.")
    input()
    print("But something is off. The castle is eerily quiet, "
          "and you can feel a dark presence lurking in the shadows.")
    input()
    print(f"We need to find the princess and escape this place. :{COMPANION}")
    input()
    print("You nod in agreement, determined to find the princess and escape the capital.")
    input()
    print("As you explore the castle, " \
          "you come across a large underground chamber filled with darkness.")
    input()
    print("In the center of the chamber, you see a pedestal with a glowing purple key.")
    input()
    print("But before you can approach the pedestal, you hear a voice calling your name.")
    input()
    print("It's the princess, but something is off.")
    input()
    print("The princess appears before you, but her eyes are glowing with a dark energy.")
    input()
    print("The princess says, 'You have come far, but you will not find your way out of here.'")
    input()
    print("The voice is distorted and twisted, "
          "and you can feel a dark presence emanating from the princess.")
    input()
    print("****************************\n"
              "  Corrupted Princess \n"
          "****************************\n")
    input()
    print("You realize that the princess has been corrupted by " \
          "the dark energy of necron, and you must fight her to escape the capital.")
    input()
    princess_choice = input("Do you want to attack the princess "
                            "or try to reason with her? (Attack/Reason): ")
    if princess_choice.strip().lower() == "reason":
        print("You try to reason with the princess, but she is too far gone.")
        input()
        death()
        return
    elif princess_choice.strip().lower() == "attack":
        print("You draw your weapon and prepare to fight the corrupted princess.")
        input()
        print("The corrupted princess lunges at you, her claws slashing through the air.")
        input()
        print("You dodge the attack and strike back, hitting the princess in the side.")
        input()
        print("The corrupted princess lets out a roar of pain and anger.")
        input()
        print("You realize that you need to find another way to defeat her, "
              "and you quickly search the chamber for a way to " \
              "disable the dark energy that is corrupting her.")
        input()
        print(f"Before either you or {COMPANION} can react,"
               "the corrupted princess lunges at you again, her claws slashing through the air.")
        input()
        princess_choice2 = input("Do you want to attack the " \
                                 "princess again or try to run away? (Attack/Run): ")
        if princess_choice2.strip().lower() == "attack":
            print(f"You and {COMPANION} attack the corrupted princess"
                  "with all your might, striking her with your weapons.")
            input()
            print("The corrupted princess roars in pain, but she is not defeated yet.")
            input()
            print("Suddenly, she summons a dark energy field that surrounds her, " \
                  "making her even more powerful and rendering your attacks useless.")
            input()
            print("You remember the book you found in the cavern, "
                  "and you quickly flip through the pages, " \
                  "searching for a spell that can help you defeat the corrupted princess.")
            input()
            print("You find a spell that seems to describe the princess, "
                  "and you quickly memorize it.")
            input()
            print("Nazma incus regina...")
            input()
            print("But before you can finish the spell, " \
                  "she lunges at you again, her claws slashing through the air.")
            input()
            death()
            return
        elif princess_choice2.strip().lower() == "run":
            print(f"You and {COMPANION} try to run away from the corrupted princess,"
                  "dodging her attacks.")
            input()
            print(f"INCOMING ATTACK!!, :{COMPANION}")
            input()
            princess_choice3 = input("Type 'DUCK' to dodge the attack: ")
            if princess_choice3.strip().lower() == "duck":
                print(f"You and {COMPANION} duck just in time,"
                      "avoiding the corrupted princess's attack.")
                input()
                print("You quickly search the chamber for a way to disable " \
                      "the dark energy that is corrupting her.")
                input()
                print("Before you can find a way to disable the dark energy, " \
                      "the book you found in the cavern starts to pulse.")
                input()
                print("It levitates into the air and opens, " \
                      "revealing a passage that seems to describe the princess.")
                input()
                print("Suddenly, lightning strikes the book, "
                      "and it begins to glow with a bright light.")
                input()
                print("The book strikes you with lightning, "
                      "and you can feel its power coursing through your veins.")
                input()
                print("You realize that you can use this power to help the corrupted princess.")
                input()
                print("You quickly memorize the passage and prepare to cast the spell.")
                input()
                print("Nazma incus regina! you chant, and a burst of light erupts from your hands.")
                input()
                print("The corrupted princess roars in pain, and you " \
                      "can see the dark energy surrounding her begin to dissipate.")
                input()
                print("AHHHHHHHHHHHHHHHHHHHHHH, NOOOOOOOOOOOOOOOO! The " \
                      "corrupted princess screams as she begins to weaken.")
                input()
                print("THIS WILL NOT BE THE END, YOU WILL NEVER ESCAPE THIS PLACE ALIVE! " \
                      " the princess screams as she falls to the ground, defeated.")
                input()
            else:
                print("You fail to dodge the attack, the " \
                      "corrupted princess strikes you down, and you fall to the ground, defeated.")
                input()
                death()
                return
        else:
            print("Invalid choice. The corrupted princess strikes you down, "
                 "and you fall to the ground, defeated.")
            input()
            death()
    else:
        print("Invalid choice. The corrupted princess strikes you down, "
              "and you fall to the ground, defeated.")
        input()
        death()

def chapter_19():
    """
    Introduces the aftermath of the corrupted princess fight and the princess's recovery
    """
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_19"
    print("***************************\n"
          "Chapter 19: The Aftermath\n"
          "***************************\n")
    input()
    print(f"You and {COMPANION} stand over the defeated corrupted princess,"
          "her body lying motionless on the ground.")
    input()
    print("You realize that you have defeated the final beast,"
           "but at a great cost.")
    input()
    print("You look down at the remains of the corrupted princess, your heart heavy with sorrow.")
    input()
    print("You begin to feel regret for what you have done.")
    input()
    print("Suddenly, you hear the princess slowly waking up")
    input()
    print("Uhhh, where am I??  as she slowly regains consciousness. :Princess Violet")
    input()
    print("What happened?, looking around the chamber. :Princess Violet")
    input()
    print("You explain to the princess that you defeated the corrupted " \
          "princess and saved her from the dark energy that corrupted her.")
    input()
    print("The princess looks at you with gratitude in her eyes.")
    input()
    print(f"Thank you, {USERNAME}, I knew you would come to save me. :Princess Violet")
    input()
    print("You help the princess to her feet, and she looks at you with a newfound determination.")
    input()
    print(f"Now, me and {COMPANION} really need to get out of here, you say to the princess.")
    input()
    print(f"Yeah, I would like to get out of here too, :{COMPANION}"
          "their voice still filled with pain.")
    input()
    print(f"You and {COMPANION} leave the chamber with the princess towards"
          "one of the castle's dungeon rooms")
    the_end()
#Goes to the end

def the_end():
    """
    Introduces the end of the game and the final choices
    """
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "the_end"
    print("***************************\n"
                   "The End\n"
          "***************************\n")
    input()
    print(f"You,{COMPANION} and the princess reach the portal that"
          "leads out of Fargon towards where you came from")
    input()
    print("The magnificent green portal is glowing with a bright light,"
          "and you can feel its power coursing through your veins.")
    input()
    print(f"Well, this is it, you and {COMPANION}"
          "say to the princess.")
    input()
    print("This is goodbye")
    input()
    print(f"Suddenly, the princess pulls you and {COMPANION} into a tight embrace.")
    input()
    print(f"Thank you, {USERNAME} and {COMPANION},"
          "for saving me and for everything you have done. :Princess Violet")
    input()
    print("Fargon will never forget your bravery and heroism. :Princess Violet")
    input()
    print(f"You and {COMPANION} nod in agreement, grateful for the princess's kind words.")
    input()
    print("Suddenly you feel a strange sensation in your chest, "
          "and you realize that you've survived so many days in Fargon")
    input()
    final_choice = input("Do you want to stay in Fargon or return home? (Stay/Return): ")
    if final_choice.strip().lower() == "stay":
        print(f"You and {COMPANION} decide to stay in Fargon,"
              "determined to continue your adventures and protect the realm.")
        input()
        print(f"You and {COMPANION} are now the heroes of Fargon,"
              "and your legend will live on for generations to come.")
        input()
        end_credits()
    #Goes to credits by choosing to stay
    elif final_choice.strip().lower() == "return":
        end_credits()
    #Returns home and goes to credits
    else:
        print(f"Invalid choice, You and {COMPANION} decide to return home,"
              "grateful for the adventures you have had in Fargon.")
        input()
        print("You say goodbye to the princess,"
              "promising to never forget your time in Fargon.")
        input()
        print(f"You and {COMPANION} step through the portal, ready to return to your world.")
        input()
        print(f"You and {COMPANION} are now the heroes of Fargon,"
              "and your legend will live on for generations to come.")
        input()
        save_game()
        end_credits()
    #Goes to credits

def end_credits():
    """
    Displays the credits and the secret ending option
    """
    print("***************************\n"
          "         Credits\n"
          "***************************\n")
    input()
    print(CREDIT_ROLL)
    input()
    print("Game made by: Eric")
    input()
    print("Goodbye!")
    input()
    secret = input("Would you like to see a secret ending? (Yes/No): ")
    if secret.strip().lower() == "yes":
        print("***************************\n"
              "secret Ending: The Dark Path\n"
              "***************************\n")
        #Seperate ending
        input()
        print(f"You and your COMPANION, {COMPANION}, decide to take a different path.")
        input()
        print("Instead of returning home, you choose to explore the dark side of Fargon.")
        input()
        print("You become the rulers of Fargon, feared and respected by all.")
        input()
        print("Your legend lives on, but it is a dark one.")
        input()
        print("You are known as the Dark Lords of Fargon, and your reign lasts for centuries.")
        input()
        print("You eventaully get defeated by a group of heroes who rise up against you.")
        input()
        print("For when there is darkness, there is light...")
        input()
        print("Thank you again. For playing this game")
        story_over()
    else:
        print("Thank you again. For playing this game")
        story_over()


def story_over():
    """
    Displays the end of the game and the final credits
    """
    ending = r"""
 .-') _    ('-. .-.   ('-.          ('-.       .-') _  _ .-') _  
(  OO) )  ( OO )  / _(  OO)       _(  OO)     ( OO ) )( (  OO) ) 
/     '._ ,--. ,--.(,------.     (,------.,--./ ,--,'  \     .'_ 
|'--...__)|  | |  | |  .---'      |  .---'|   \ |  |\  ,`'--..._)
'--.  .--'|   .|  | |  |          |  |    |    \|  | ) |  |  \  '
   |  |   |       |(|  '--.      (|  '--. |  .     |/  |  |   ' |
   |  |   |  .-.  | |  .--'       |  .--' |  |\    |   |  |   / :
   |  |   |  | |  | |  `---.      |  `---.|  | \   |   |  '--'  /
   `--'   `--' `--' `------'      `------'`--'  `--'   `-------'  """
    for char in ending:
        print(char, end="")
        #Prints out every character one by one
    keyboard = r"""
 ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ 
||C |||R |||E |||A |||T |||E |||D |||       |||B |||Y ||
||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|
 ____ ____ ____ ____                                    
||E |||R |||I |||C ||                                   
||__|||__|||__|||__||                                   
|/__\|/__\|/__\|/__\|                                    """
    for char in keyboard:
        print(char, end="")
        final_choice = input("Would you like to start over? (Yes/No): ")
        if final_choice.strip().lower() == "yes":
            print("Starting over...")
            input()
            main()
        elif final_choice.strip().lower() == "no":
            print("Thank you for playing!")
            input()
            exit()
        else:
            print("Invalid choice. Exiting the game.")
            input()
            exit()
#Prints each character one by one, takes a while
#End of game
if __name__ == "__main__":
    main()
#Used due to multiple functions
