"""
TalesOfTime: A text-based adventure game where you defeat 5 bosses
and 3 secret bosses to save Fargon
"""
# GameName TalesOfTime
# StudentName EricZheng
# GameDuration: This game should go for around an hour on average.
# Uses Upper_Case naming style for constants and snake_case for functions and variables
# Imports
import time
import random
import json
# Imports time for time control and time.sleep,
# random for the random health decrease and json to make json file to save progress

# Global variables to be used throughout the game
USERNAME = ""
COMPANION = ""
PLAYER = None  # Will be initialized with playerdata()
CURRENT_CHAPTER = ""

# Ascii art
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

SAVE_FILE = "TalesOfTimeSave.json"
#This gives the save file a name


def save_game():
    """Used to save game to a json file"""
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
    """Used to extract data from the Json file and load"""
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
    """Used to resume the game"""
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
    elif CURRENT_CHAPTER == "Necron_fight":
        necron_fight()
    elif CURRENT_CHAPTER == "Necron_fight2":
        necron_fight2()
    elif CURRENT_CHAPTER == "Necron_fight3":
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
    elif CURRENT_CHAPTER == "Necron_fight4":
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
    """Used to decrease the player's health"""
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
    """Used to increase the player's health"""
    if PLAYER is None:
        print("Error: PLAYER not initialized.")
        death()
        return
    PLAYER["health"] += amount
    print(f"Your health is now {PLAYER['health']}")
#This function increases the PLAYER's health

def reset_health():
    """Used to reset the player's health"""
    if PLAYER is None:
        print("Error: PLAYER not initialized.")
        death()
        return
    PLAYER["health"] = 100
    print("Your health has been reset to 100.")
#This function resets the PLAYERs health

def playerdata(name):
    """The player's data for their stats by default"""
    return {"name": name,
            "health": 100,
            "gold": 200,
            "strength": 20,
            "defence": 20,
            "luck": 20,}
#This function shows the PLAYER's stats. Still in work


def decrease_gold(amount):
    """Used to decrease the player's gold"""
    if PLAYER is None:
        print("Error: PLAYER not initialized.")
        death()
        return
    PLAYER["gold"] -= amount
    print(f"You spent {amount} gold. Your gold is now {PLAYER['gold']}.")
#This function lowers the PLAYERs gold

def increase_gold(amount):
    """Used to increase the player's gold"""
    if PLAYER is None:
        print("Error, PLAYER is not intitialized.")
        death()
        return
    PLAYER["gold"] += amount
    print(f"You gained {amount} gold. Your gold is now {PLAYER['gold']}")
#This function increases the PLAYER's gold

def death():
    """Used to kill the player"""
    print("You have died. Game over.")
    time.sleep(2)
    print("Do you want to restart the game? (Yes/No): ")
    choice = input().strip().lower()
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
    """Used to restart the game and go to main"""
    global USERNAME, COMPANION, PLAYER
    print("restarting the game...")
    USERNAME = ""
    PLAYER = None
    COMPANION = ""
    main()
#This function restarts the game

def dark_dagger_story():
    """Shows the dagger being upgraded and shows backstory"""
    print("Before you leave, you notice a bottle of ominous energy.")
    time.sleep(5)
    print("Suddenly your dagger flies out your hand and forges with the ominous energy")
    time.sleep(5)
    print("'You have acquired 'Darkness's Scale'")
    time.sleep(5)
    print(DARK_DAGGER)
    learn_more1 = input("Would you like to hear about the backstory of this weapon (Yes/No)?")
    match learn_more1.lower().strip():
        case "yes":
            print("This dagger, now corrupted by dark energy. " \
                  "Has increased sharpness and toughness allowing it attack " \
                  "against even the strongest of enemies.")
            time.sleep(5)
            chapter_7()
            return
        case "no":
            print("Ok, skipping backstory")
            time.sleep(5)
            chapter_7()
            return
        case _:
            print("Invalid Option")
            print("Try Again")
            dark_dagger_story()
            return
#This is for the upgrade of the dagger

def dark_sword_story():
    """Used to upgrade sword and to show backstory"""
    print("Before you leave, you notice a bottle of ominous energy.")
    time.sleep(5)
    print("Suddenly your sword flies out your hand and forges with the ominous energy")
    time.sleep(5)
    print("'You have acquired 'The Corrupted Sword'")
    time.sleep(5)
    print(DARK_SWORD)
    learn_more2 = input("Would you like to hear about the backstory of this weapon (Yes/No)?")
    match learn_more2.lower().strip():
        case "yes":
            print("This sword, now corrupted by dark energy. " \
                  "Has increased sharpness and toughness allowing " \
                  "it attack against even the strongest of enemies.")
            time.sleep(5)
            chapter_10()
            return
        case "no":
            print("Ok, skipping backstory")
            time.sleep(5)
            chapter_10()
            return
        case _:
            print("Invalid Option")
            print("Try Again")
            dark_sword_story()
            return
#This is for the upgrade of the sword


def dark_shield_story():
    """Used to upgrade shield and to show backstory"""
    print("Before you leave, you notice a bottle of ominous energy.")
    time.sleep(5)
    print("Suddenly your shield flies out your hand and forges with the ominous energy")
    time.sleep(5)
    print("'You have acquired 'The Dark Shield'")
    time.sleep(5)
    print(DARK_SHIELD)
    learn_more3 = input("Would you like to hear about the backstory of this weapon (Yes/No)?")
    match learn_more3.lower().strip():
        case "yes":
            print("This shield, now corrupted by dark energy. " \
                  "Has increased defence and toughness allowing it defend " \
                  "against even the strongest of enemies.")
            time.sleep(5)
            chapter_12()
            return
        case "no":
            print("Ok, skipping backstory")
            time.sleep(5)
            chapter_12()
            return
        case _:
            print("Invalid Option")
            print("Try Again")
            dark_shield_story()
            return
#This is for the upgrade of the shield

#Start of game with title screen
def main():
    """Start of the game"""
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
        match result.lower().strip():
            case "enter":
                USERNAME = input("Enter your name: ")
                PLAYER = playerdata(USERNAME)
                time.sleep(2)
                print("You woke up in a strange place, with no memory of how you got there.")
                time.sleep(2)
                print("You look around and see a path leading into the distance.")
                time.sleep(2)
                print("You decide to follow it, hoping to find some answers.")
                time.sleep(2)
                print("As you walk, you notice the surroundings changing. " \
                      "The path becomes narrower, "
                      "and the trees around you grow taller and denser. " \
                      "You feel a sense of unease but continue on.")
                time.sleep(2)
                print('Suddenly, you hear a rustling sound behind you. ' \
                      'You turn around quickly, but there is nothing there. ')
                time.sleep(2)
                print('You shake your head, trying to dismiss the feeling of being watched.')
                time.sleep(2)
                print('You can leave or continue on your journey.')
                choice = input("What do you want to do (Leave/Continue)? ")
                match choice.lower().strip():
                    case "leave":
                        print("You chose not to continue. " \
                              "You sit down waiting for something to happen.")
                        time.sleep(5)
                        print("Nothing happen, You die of boredom")
                        time.sleep(5)
                        death()
                #This kills the PLAYER since they typed in that they want to leave
                    case "continue":
                        print("You chose to continue. Moving forward...")
                        save_game()
                        companion_chapter()
                #This continues to the next chapter
                    case _:
                        print("Invalid Option")
                        time.sleep(5)
                        print("Try Again")
                #This makes the PLAYER try again
        #This is the option when the PLAYER types in enter or presses enter
            case "tutorial":
                print("This will restart the game!")
                time.sleep(5)
                print("This is a text based game.")
                time.sleep(5)
                print("Normally, you will wait 5 seconds until the next text loads.")
                time.sleep(5)
                print("If there is a question, " \
                      "type a response that is shown on the screen, "
                      "or you will have to try again.")
                time.sleep(5)
                print("If you choose a bad option, " \
                      "then you would most likely die to reflect what would happen in real life.")
                time.sleep(5)
                print("There a 5 Bosses to beat as well as 3 secret bosses.")
                time.sleep(5)
                print("Remember, this game requires patience so don't"
                      "press anything until it says so!")
                time.sleep(2)
                print("Also, the game will autosave progress onto a " \
                      "JSON file after you complete a chapter."
                      "So if you die, you can still go back to your progress!")
                time.sleep(5)
                print("THIS DOESN'T SAVE ANY PROGRESS IF YOU HAVENT FINISHED THE FIRST CHAPTER")
                time.sleep(5)
                print("To do that type 'Load' on the Welcome text."
                      "That will bring back your progress!")
                time.sleep(2)
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
    """Introduces companion to you"""
    global COMPANION, CURRENT_CHAPTER
    CURRENT_CHAPTER = "companion_chapter"
    time.sleep(2)
    print("Suddenly, out of the blue, a mysterious character " \
          "jumps out from a bush holding a dagger ready to attack you.")
    time.sleep(5)
    companion_choice = input("You can either type 'Kill' to kill him or " \
                             "type 'Reason' to reason with him: ")
    if companion_choice.lower() == "kill":
        print("You tried killing the mysterious character " \
              "but they proceed to strike you in the stomach.")
        time.sleep(5)
        print("You fall to the ground, " \
              "bleeding out and unable to move...")
        time.sleep(5)
        print("The mysterious character stands over you, " \
              "looking down with a mix of pity and regret.")
        time.sleep(5)
        print("You realize that you have made a grave mistake, "
              "and your life is now forfeit.")
        time.sleep(5)
        decrease_health()
        print("You pass out from the pain and lose consciousness.")
        time.sleep(10)
        print("When you wake up you find yourself in a cave resting " \
              "on the floor with the mysterious character standing nearby.")
        time.sleep(5)
        print("He notices you are awake and runs off into the darkness, " \
              "leaving you alone in the cave.")
        time.sleep(5)
        print("You died of loneliness and despair.")
        death()
        return
    #This kills the PLAYER when they try to kill the enemy
    elif companion_choice.lower() == 'reason':
        print("Reasoning with the mysterious character, " \
              "you explain that you mean no harm and are also lost in this strange place...")
        time.sleep(10)
        print("The mysterious character agrees and joins you on your " \
              "journey to get out of this foreign place.")
        time.sleep(5)
        print("The mysterious character is now your Companion.")
        time.sleep(5)
        print("Before continuing, you ask the mysterious character his name.")
        COMPANION = input("Enter Companion's name: ")
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
    """Companion needs help to find their stuff"""
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_1"
    print(f"***************************\n"
         f"Chapter 1: {COMPANION}'s Dilemma\n"
           "***************************\n")
    time.sleep(2)
    print(f'You and {COMPANION} continue down the path, discussing your situation.')
    time.sleep(5)
    print(f"'You know, I know a way out of here, but I need your help first,' :{COMPANION}.")
    time.sleep(5)
    dagger_choice = input("During our little scuffle, I lost my dagger."
                          f"Can you help me find it? :{COMPANION}(Yes/No): ")
    if dagger_choice.lower() == "yes":
        print(f"Thank you! I knew I could count on you! :{COMPANION}")
        time.sleep(2)
        print(f"You and {COMPANION} start searching the area for the lost dagger.")
        time.sleep(10)
        print("After a while, you find the dagger hidden under some leaves.")
        time.sleep(5)
        print(f"You hand the dagger back to {COMPANION}, who looks relieved.")
        time.sleep(5)
        print(f"Here, {USERNAME} take my dagger,"
              f"I see you have no weapon. Follow me, {USERNAME}. :{COMPANION}")
        time.sleep(5)
        print(f"You acquired {COMPANION}'s trusty dagger.")
        time.sleep(5)
        print(SPECIAL_DAGGER)
        time.sleep(5)
        save_game()
        chapter_2()
        return
    #This continues the game since the PLAYER wants to help COMPANION
    else:
        print(f"Too bad, I guess you don't want to leave this place... :{COMPANION}")
        time.sleep(10)
        print(f"{COMPANION} turns away and walks off into the darkness, leaving you alone.")
        time.sleep(5)
        print("You died of loneliness and despair.")
        death()
        return
    #This kills the PLAYER since they don't want to help

def chapter_2():
    """Companion tells you about the backstory of Fargon"""
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_2"
    print("***************************\n"
       "Chapter 2: The Lost Princess of Faron\n"
          "***************************\n")
    time.sleep(5)
    print("Ok, so you see, This place is called Faron,"
            "it used to be a beautiful place,"
          f"ruled by a princess called Violet. :{COMPANION}")
    time.sleep(5)
    print("But now, it's just a shadow of its former self,"
          f"plagued by dark creatures and monsters. :{COMPANION}")
    time.sleep(5)
    print(f"As you and {COMPANION} walk, you can feel"
           "the weight of the history around you.")
    time.sleep(5)
    print("You see ruins of old buildings, broken statues, "
          "and remnants of a once-thriving civilization in the distance.")
    time.sleep(5)
    print(f"You ask {COMPANION} about Princess Violet and what happened to her.")
    time.sleep(5)
    print(f"{COMPANION} looks sad 'The princess was taken by"
          f"the monsters that consumed this place. :{COMPANION}")
    time.sleep(5)
    print(f"She was the last hope for Faron, but now she's gone. :{COMPANION}")
    time.sleep(5)
    print("You feel a sense of determination to find a way to save Faron and its lost princess.")
    time.sleep(5)
    print(f"You ask {COMPANION} how do they know all this.")
    time.sleep(5)
    print("'I arrived a few years ago, and I have been trying"
          f"to find a way out ever since. :{COMPANION}'")
    time.sleep(5)
    print("I have heard stories from the locals about the princess"
          f"and the monsters that took her. :{COMPANION}")
    time.sleep(5)
    print(f"You ask {COMPANION} where the princess is at now?")
    time.sleep(5)
    print("I don't know, but I have heard rumors of a hidden temple deep in the forest." /
          "It's said that the princess is trapped there,"
          f"guarded by powerful creatures. :{COMPANION}")
    time.sleep(5)
    path_choice = input("You have a choice to make." \
                        "Do you want to go to the temple and try " \
                        "to rescue the princess? (Yes/No): ")
    if path_choice.lower() == "yes":
        print(f"You and {COMPANION} set off towards the hidden temple,"
              "determined to rescue the princess.")
        time.sleep(5)
        save_game()
        time.sleep(5)
        chapter_3()
        return
    #This goes to the next chapter since the PLAYER wants to progress
    else:
        print("You decide not to take the risk and continue on your current path.")
        time.sleep(5)
        print("All of a sudden, you hear a loud roar and a bull appears out of nowhere.")
        time.sleep(5)
        print(BULL)
        time.sleep(5)
        bull_fight = input("You can either type 'Run' to run away or " \
                           "type 'Fight' to fight the bull: ")
        if bull_fight.lower() == "run":
            print("You turn and run as fast as you can, escaping the bull's charge.")
            time.sleep(5)
            print("Unfortunately, you run into a dead end and the bull catches up to you.")
            time.sleep(5)
            death()
            return
        #This kills the PLAYER as the bull kills them
        elif bull_fight.lower() == "fight":
            print("You bravely stand your ground and prepare to fight the bull.")
            time.sleep(5)
            print("You regret your choice")
            time.sleep(5)
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
    """Introducs the mechanics and what the battles will feel like, with the first dungeon"""
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_3"
    while True:
        print("***************************\n"
              "Chapter 3: The Hidden Temple\n"
              "***************************\n")
        #Introduction to the dungeon
        time.sleep(2)
        print(DUNGEON_1)
        #This prints the ascii art for the dungeon
        print(f"You and {COMPANION} arrive at the hidden temple,"
              "its entrance shrouded in vines and darkness.")
        time.sleep(5)
        print("As you step inside, you feel a chill run down your spine. " \
              "The air is thick with dust and the smell of decay.")
        time.sleep(5)
        print("You can hear the faint sound of water dripping in the distance, " \
              "echoing through the empty halls.")
        time.sleep(5)
        print(f"You and {COMPANION} cautiously explore the temple,"
              "searching for any signs of the princess.")
        time.sleep(5)
        print("'Here, {USERNAME} take this sword as well as this shield,"
              f"Stay cautious, I don't have a good feeling about this...' :{COMPANION}")
        time.sleep(5)
        print(f"You have acquired {COMPANION}'s special iron sword and reinforced shield")
        time.sleep(5)
        print(SPECIAL_SHIELD)
        time.sleep(5)
        print(SPECIAL_SHIELD)
        time.sleep(5)
        print("Suddenly, you hear a loud roar and a " \
              "giant creature appears in front of you, blocking your path.")
        time.sleep(5)
        print("The creature is a massive stone golem, its eyes glowing with an eerie light.")
        time.sleep(5)
        print(f"All of a sudden, the golem charges at {COMPANION} and knocks them to the wall")
        time.sleep(5)
        print("****************************\n"
              " Forging The Beast of Stone \n"
              "****************************\n")
        #Introduction to the boss
        print(GOLEM)
        #This prints the ascii for the golem, this repeats for all the bosses
        time.sleep(5)
        print("You have a choice to make. Do you want to fight the golem "
              "or try to reason with it? (Fight/Reason): ")
        golem_choice = input("What do you want to do? ")
        if golem_choice.lower() == "fight":
            print("You bravely stand your ground and prepare to fight the golem.")
            time.sleep(5)
            print("It charges at you, swinging its massive fists.")
        #This continues to the next attack sequence
        elif golem_choice.lower() == "reason":
            print("You try to reason with the golem, explaining that " \
                  "you mean no harm and are only looking for the princess.")
            time.sleep(5)
            print("Never do that again, the golem doesn't speak English, it does speak with fists")
            time.sleep(5)
            print("The golem knocks you out cold")
            time.sleep(5)
            death()
            return
        #This kills the PLAYER since they tried reasoning with a rock
        else:
            print("Invalid choice. The golem charges at you!")
            time.sleep(5)
            death()
            return
        #This kills the PLAYER since they did an invalid response
        while True:
            golem_choice2 = input("You can either type 'Dodge' to dodge its attack "
                                  "or type 'Attack' to attack it: ")
            if golem_choice2.lower() == "dodge":
                print("You quickly dodge the golem's attack, narrowly avoiding its powerful fists.")
                time.sleep(5)
                print("You counterattack, striking the golem with all your might.")
                time.sleep(5)
                print("The golem staggers back, but it is not defeated yet."
                      f"You and {COMPANION} must work together to defeat it.")
                time.sleep(5)
                save_game()
                chapter_3part2()
                return
            #This continues to the next chapter
            elif golem_choice2.lower() == "attack":
                print("You charge at the golem, swinging your weapon with all your might.")
                time.sleep(5)
                print("The golem retaliates with a powerful punch, " \
                      "sending you flying across the room.")
                time.sleep(5)
                death()
                return
            #This kills the PLAYER
            else:
                print("Invalid choice. The golem charges at you!")
                time.sleep(5)
                death()
                return
            #This kills the PLAYER for an invalid response

def chapter_3part2():
    """Part 2 of Chapter 3, battle continues"""
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_3part2"
    while True:
        golem_choice3 = input("You can either type 'Attack' to attack the golem again"
                              f"or type 'Heal' to wake up {COMPANION}: ")
        if golem_choice3.lower() == "attack":
            print(f"You and {COMPANION} attack the golem with all your might.")
            time.sleep(5)
            print("The golem stands unfazed, cracks form but it is still standing.")
            time.sleep(5)
            print("You realize that you need to find a way to weaken it before you can defeat it.")
        #This repeats the question again
        elif golem_choice3.lower() == "heal":
            print(f"You use a healing potion to wake up {COMPANION}.")
            time.sleep(5)
            print(f"{COMPANION} is back in the fight!")
            print("You both attack the golem together, striking it with all your might.")
            time.sleep(5)
            print("The golem staggers back, its stone body cracking under your combined assault.")
            time.sleep(5)
            print("You both continue to attack the golem, striking it with all your might.")
            time.sleep(5)
            print("Finally, with one last powerful blow, " \
                  "the golem crumbles to the ground, defeated.")
            time.sleep(5)
            print(f"You and {COMPANION} stand victorious,"
                   "breathing heavily from the intense battle.")
            time.sleep(5)
            print("You search the golem's remains and find a rusty grey key " \
                  "that unlocks a hidden door in the temple.")
            time.sleep(5)
            print(f"You and {COMPANION} enter the hidden door, hoping to find the princess inside.")
            time.sleep(5)
            print("As you step through the door, you find yourselves in " \
                  "a dimly lit chamber filled with ancient artifacts.")
            time.sleep(5)
            print("In the center of the room, you see a pedestal with a glowing golden key.")
            time.sleep(5)
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
    """Tells more backstory about the keys"""
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_4"
    while True:
        print("***************************\n"
              "Chapter 4: The Path Ahead\n"
              "***************************\n")
        time.sleep(2)
        print(f"You and {COMPANION} exit the temple past the pile of"
               "rubble and continue down a path.")
        time.sleep(5)
        key_question = input(f"You can ask {COMPANION} a question about the other keys"
                              "or continue down the path playing with the key. (Ask/Continue): ")
        if key_question.lower() == "ask":
            print(f"You ask {COMPANION} about the other keys.")
            time.sleep(5)
            print(f"'There are 5 keys in total, but I don't know the exact locations,"
                  f"but I have heard rumors of their existence' :{COMPANION}")
            time.sleep(5)
            print("Suddenly, the key shifts in you hand and points forwards.")
            time.sleep(5)
            print(f"You thank {COMPANION} for the information and continue down the path.")
            time.sleep(5)
            print(f"The path ahead changes to a lush green tropical forest but you and"
                  f"{COMPANION} are determined to find the other keys and rescue the princess.")
            save_game()
            chapter_5()
            break
        #This continues to the next dungeon while showing a little more backstory
        elif key_question.lower() == "continue":
            print("You decide to continue down the path, playing with the key you found.")
            time.sleep(5)
            print("The key feels warm in your hand, and you can sense its power.")
            time.sleep(5)
            print(f"The path ahead changes to a lush green tropical forest but you and {COMPANION}"
                   "are determined to find the other keys and rescue the princess.")
            save_game()
            time.sleep(5)
            save_game()
            chapter_5()
            break
        #This skips the backstory but still goes to the next dungeon
        else:
            print("Invalid choice, Try again")
        #This asks the question again in a loop until they ask a valid response
#This is to bring a small break between the dungeons

def chapter_5():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_5"
    print("***************************\n"
          "Chapter 5: The Goblin Camp\n"
          "***************************\n")
    time.sleep(2)
    print(f"You and {COMPANION} arrive at the goblin camp,"
           "a makeshift settlement hidden deep in the forest.")
    time.sleep(5)
    print("As you enter, you can feel the tension in the air. " \
          "The goblins eye you suspiciously, their weapons at the ready.")
    time.sleep(5)
    print("You know that this will be a difficult challenge, " \
          "but you are determined to find the next key.")
    time.sleep(5)
    print("We need to be careful."
          f"The goblins are known for their traps and ambushes. :{COMPANION}")
    time.sleep(5)
    print("You nod in agreement and start to plan your approach.")
    time.sleep(5)
    print(f"Stay here, I'll go talk to the camp chief"
          f"and see if they know anything about the key. :{COMPANION}")
    time.sleep(5)
    print(f"{COMPANION} disappears around the corner of a hut, leaving you alone in the camp.")
    time.sleep(5)
    goblin_choice = input("Now you have a choice to make."
                          f"Do you want to wait for {COMPANION} to return"
                           "or explore the camp on your own? (Wait/Explore): ")
    if goblin_choice.lower() == "wait":
        print(f"You decide to wait for {COMPANION} to return.")
        time.sleep(5)
        print(f"{COMPANION} returns after a while, looking worried.")
        time.sleep(5)
        print("The goblin chief knows where the dungeon is,"
              f"but he won't give it up easily. :{COMPANION}")
        time.sleep(5)
        print(f"You approach the chief with {COMPANION}")
        time.sleep(5)
        goblin_choice2 = input("Do you want to try to reason with " \
                               "the goblin chief or attack him? (Reason/Attack): ")
        while True:
    #Waiting for COMPANION to come back and the going to the chief
            if goblin_choice2.lower() == "reason":
                print(f"You and {COMPANION} approach the goblin chief, trying to reason with him.")
                time.sleep(5)
                print("The goblin chief listens to your plea, but he is not convinced.")
                time.sleep(5)
                print(f"We need to find another way to get the location :{COMPANION}")
                time.sleep(5)
                print("You nod in agreement and start to plan your next move.")
                time.sleep(5)
                print("You decide to explore the camp further, " \
                      "hoping to find some clues about the location.")
                time.sleep(5)
        #loops again to the goblin chief question
            elif goblin_choice2.lower() == "attack":
                print(f"You and {COMPANION} decide to attack the goblin chief.")
                time.sleep(5)
                print("The goblin chief fights back fiercely, " \
                      "but you manage to defeat him after a tough battle.")
                time.sleep(5)
                print("You search the goblin chief's hut and find a map " \
                      "that leads to the next dungeon.")
                time.sleep(5)
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
            time.sleep(5)
            print("As you look around, you notice a few goblins eyeing you suspiciously.")
            time.sleep(5)
            print("Nonetheless, you continue to explore, hoping to find some clues about the key.")
            time.sleep(5)
            print("You find a small windmill with a sign that reads 'Storage Space'.")
            time.sleep(5)
            print(GOBLIN_HUT)
            goblin_choice3 = input("Do you want to enter the windmill? (Yes/No): ")
            if goblin_choice3.lower() == "yes":
                while True:
                    time.sleep(5)
                    print("You enter the hut and find a chest in the corner.")
                    time.sleep(5)
                    print("You open the chest and find a dusty yellow map inside.")
                    time.sleep(5)
                    print("You take the map and return to the main camp area.")
                    time.sleep(5)
                    print(f"You find {COMPANION} waiting for you, looking relieved.")
                    time.sleep(5)
                    print(f"I was worried about you."
                          f"Did you find anything useful? :{COMPANION}")
                    time.sleep(5)
                    print(f"You show {COMPANION} the map you found in the hut.")
                    time.sleep(5)
                    print(f"{COMPANION} looks at the map"
                          "This looks like to the next dungeon"
                          f"It might help us find the key! :{COMPANION}")
                    save_game()
                    chapter_6()
                    break
            #Goes to the dungeon
            elif goblin_choice3.lower() == "no":
                print("You decide not to enter the windmill and continue exploring the camp.")
                time.sleep(5)
                print("You wander around, but you don't find anything else of interest.")
                time.sleep(5)
                print("You return to the main camp area,"
                      f"where you find {COMPANION} waiting for you.")
                time.sleep(5)
                print(f"Did you find anything useful? :{COMPANION}")
                time.sleep(5)
                print(f"You tell {COMPANION} that you didn't find anything,"
                      "but you feel like you might have missed something important.")
                time.sleep(5)
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
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_6"
    while True:
        print("***************************\n"
            "Chapter 6: The Crystal Dungeon\n"
              "***************************\n")
        time.sleep(2)
        print(DUNGEON_2)
        time.sleep(2)
        print(f"You and {COMPANION} arrive at the entrance of the lush green cavern,"
              "the second dungeon.")
        time.sleep(5)
        print("The air is thick with moisture, "
              "and you can hear the sound of dripping water echoing through the darkness.")
        time.sleep(5)
        print("You light a torch and step inside, " \
              "the flickering light revealing jagged rocks and narrow passages.")
        time.sleep(5)
        print("Be careful. This place is known for its"
              f"traps and dangerous creatures. :{COMPANION}")
        time.sleep(5)
        print("You nod and start to explore the cavern, searching for the key.")
        time.sleep(5)
        print("As you venture deeper, you come across a large underground lake.")
        time.sleep(5)
        print("In the center of the lake, you see a small island with a pedestal on it.")
        time.sleep(5)
        print("On the pedestal, you can see a glimmering blue key.")
        time.sleep(5)
        print(f"You and {COMPANION} realize that this must be the second key you are looking for.")
        time.sleep(5)
        print("Before either of you could react, " \
              "a giant beast emerges from the water, its eyes glowing with a menacing light.")
        time.sleep(5)
        print("The beast is a massive serpent, its scales glistening in the water")
        time.sleep(5)
        print("****************************\n"
              "Serpus The Beast of the Lake \n"
              "****************************\n")
        print(SERPUS)
        #Shows ascii art of the serpus
        time.sleep(5)
        print("Before either of you could move, Serpus strikes you both in the back.")
        decrease_health()
        print(f"{COMPANION}'s health is low")
        time.sleep(5)
        serpent_choice = input("Serpus is charging up it's next attack, (Attack/Dodge): ")
        #User's input is stored as serpent_choice
        if serpent_choice.lower() == "attack":
            print("Serpus strikes you in the stomach and injures you.")
            time.sleep(5)
            decrease_health()
            print(f"{COMPANION}'s health is low")
            time.sleep(5)
            print(f"You and {COMPANION} are both injured"
                  "and need to find a way to defeat Serpus before it attacks again.")
            time.sleep(5)
            save_game()
            serpus_fight3()
        #Goes to next the final sequence
        elif serpent_choice.lower() == "dodge":
            print("You quickly dodge Serpus's attack, narrowly avoiding its powerful strike.")
            time.sleep(5)
            print("You counterattack, striking Serpus with all your might.")
            time.sleep(5)
            print("The serpent staggers back,"
                  "but it is not defeated yet."
                  f"You and {COMPANION} must work together to defeat it.")
            time.sleep(5)
            save_game()
            serpus_fight2()
        #Goes to the next sequence
        else:
            print("Invalid choice. Serpus attacks you again!")
            death()
        #Kills the PLAYER since they didn't respond properly

def serpus_fight2():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "serpus_fight2"
    while True:
        serpent_choice2 = input("You can either type 'Attack' to attack Serpus"
                                f"or type 'Heal' to heal yourself and {COMPANION}: ")
        #User's input is stored as serpentchoice2
        if serpent_choice2.lower() == "attack":
            print(f"You and {COMPANION} attack Serpus with all your might,"
                  "striking it with your weapons.")
            time.sleep(5)
            print("Finally, with one last powerful blow, " \
                  "Serpus roars in pain and sinks back into the depths of the lake.")
            time.sleep(5)
            print(f"You and {COMPANION} stand victorious,"
                  "breathing heavily from the intense battle.")
            time.sleep(5)
            print("You search the serpent's remains and find a glimmering blue key " \
                  "that unlocks a hidden door in the cavern.")
            time.sleep(5)
            print(f"You and {COMPANION} enter the hidden door,"
                  "hoping to find the next key inside.")
            time.sleep(5)
            print("As you step through the door, " \
                  "you find yourselves in a dimly lit chamber filled with ancient artifacts.")
            time.sleep(5)
            print("In the center of the room, you see a pedestal with a glowing blue key.")
            time.sleep(5)
            print("****************************\n"
                   "  2 Key Achieved 3 left. \n"
                  "****************************\n")
            print(f"You and {COMPANION} take the key and prepare to continue your journey.")
            time.sleep(5)
            save_game()
            dark_dagger_story()
            #Shows the dagger upgrade story
            return
        elif serpent_choice2.lower() == "heal":
            print(f"You use a healing potion to heal yourself and {COMPANION}.")
            time.sleep(5)
            print(f"{COMPANION} is back in the fight!")
            time.sleep(5)
            print("You both attack Serpus together, striking it with all your might.")
            time.sleep(5)
            print("Serpus slithers back, its slimy scales cracking under your combined assault.")
            time.sleep(5)
            print("You both continue to attack Serpus, striking it with all your might.")
            time.sleep(5)
            print("Finally, with one last powerful blow, Serpus collapses to the ground, defeated.")
            time.sleep(5)
            print(f"You and {COMPANION} stand victorious,"
                  "breathing heavily from the intense battle.")
            time.sleep(5)
            print("You search Serpus's remains and find a mysterious " \
                  "blue key that unlocks a hidden door in the temple.")
            time.sleep(5)
            print(f"You and {COMPANION} enter the hidden door, hoping to find the princess inside.")
            time.sleep(5)
            print("As you step through the door, you find yourselves "
                  "in a dimly lit chamber filled with ancient artifacts.")
            time.sleep(5)
            print("In the center of the room, you see a pedestal with a glowing blue key.")
            time.sleep(5)
            print("****************************\n"
                   "  2 Key Achieved 3 left. \n"
                  "****************************\n")
            print(f"You and {COMPANION} take the key and prepare to continue your journey...")
            time.sleep(5)
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
    global CURRENT_CHAPTER
    # These are global variables for the saving function,
    # PLAYER USERNAME, PLAYER stats, COMPANION USERNAME
    # allowing for these functions to work within the different chapters
    CURRENT_CHAPTER = "serpus_fight3"
    serpent_choice3 = input("Type 'Attack' to attack Serpus again or"
                            f"type 'Heal' to heal yourself and {COMPANION}: ")
    if serpent_choice3.lower() == "attack":
        print(f"You and {COMPANION} attack Serpus's core with all your might,"
              "striking it with your weapons.")
        time.sleep(5)
        print("Serpus roars in pain, and it smashes into the ground, defeated.")
        time.sleep(5)
        print(f"You and {COMPANION} stand victorious, breathing heavily from the intense battle.")
        time.sleep(5)
        print("You search the serpent's remains and find a glimmering " \
              "blue key that unlocks a hidden door in the cavern.")
        time.sleep(5)
        print(f"You and {COMPANION} enter the hidden door, hoping to find the next key inside.")
        time.sleep(5)
        print("As you step through the door, you find yourselves "
              "in a dimly lit chamber filled with ancient artifacts.")
        time.sleep(5)
        print("In the center of the room, you see a pedestal with a glowing blue key.")
        time.sleep(5)
        print("****************************\n"
              "  2 Key Achieved 3 left. \n"
              "****************************\n")
        print(f"You and {COMPANION} take the key and prepare to continue your journey...")
        time.sleep(5)
        save_game()
        dark_dagger_story()
        chapter_7()
            #This shows the dagger upgrade story
    elif serpent_choice3.lower() == "heal":
        print(f"You use a healing potion to heal yourself and {COMPANION}.")
        print("Serpus lunges at you before either of you could attack.")
        death()
        #This kills the PLAYER
    else:
        print("Invalid choice. Serpus attacks you again!")
        death()
        #This kills the PLAYER since they entered an invalid response

def chapter_7():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_7"
    print("***************************\n"
    "Chapter 7: The Path to the Fire Dungeon\n"
          "***************************\n")
    time.sleep(2)
    print(f"You and {COMPANION} exit the jungle cavern and continue down the path,"
          "the lush greenery giving way to rocky terrain.")
    time.sleep(5)
    print("The air grows hotter, and you can feel the heat radiating from the ground.")
    time.sleep(5)
    print("The next key is said to be hidden in a fire dungeon,"
          f"deep within the mountains according to the map. :{COMPANION}")
    time.sleep(5)
    print("You nod in agreement, determined to find the next key and rescue the princess.")
    time.sleep(5)
    print("As you continue down the path, you come across a group of goblins blocking your way.")
    time.sleep(5)
    print("The goblins are armed with crude weapons and look ready for a fight.")
    time.sleep(5)
    print("We need to be careful."
          f"The goblins are known for their traps and ambushes. :{COMPANION}")
    time.sleep(5)
    goblin_offer = input("Do you want to fight the goblins "
                         "or try to reason with them? (Fight/Reason): ")
    if goblin_offer.lower() == "fight":
        print(f"You and {COMPANION} charge at the goblins, weapons drawn.")
        time.sleep(5)
        print("The goblins fight back fiercely,"
              f"but you and {COMPANION} are able to defeat them after a tough battle.")
        time.sleep(5)
        print("You search the goblins' remains and find a map that leads to the fire dungeon.")
        time.sleep(5)
        print(f"You and {COMPANION} take the map and prepare to continue your journey.")
        time.sleep(5)
        save_game()
        chapter_8()
        #This moves to the next chapter
    elif goblin_offer.lower() == "reason":
        print("You try to reason with the goblins, " \
              "explaining that you mean no harm and are only looking for the next key.")
        time.sleep(5)
        print("The goblins listen to your words, but they are still wary of you.")
        time.sleep(5)
        print(f"{COMPANION} suggests that you offer them something in exchange for safe passage.")
        time.sleep(5)
        goblin_offer2 = input("Do you want to offer them some of your supplies? (Yes/No): ")
        if goblin_offer2.lower() == "yes":
            print("You offer the goblins some of your supplies, and they accept your offer.")
            time.sleep(5)
            print(f"The goblins allow you and {COMPANION}"
                  "to pass safely, and you continue on your journey.")
            time.sleep(5)
            save_game()
            chapter_8()
        #This moves to the next chapter
        elif goblin_offer.lower() == "no":
            print("The goblins refuse to let you pass without a fight.")
            time.sleep(5)
            print(f"You and {COMPANION} are forced to fight the goblins,"
                   "but you are able to defeat them after a tough battle.")
            time.sleep(5)
            decrease_health()
            time.sleep(5)
            print("You search the goblins' sacks and find a map that leads to the fire dungeon.")
            time.sleep(5)
            print(f"You and {COMPANION} take the map and prepare to continue your journey.")
            time.sleep(5)
            save_game()
            chapter_8()
        #This moves to the next chapter
        else:
            print("Invalid choice. You continue down the path without making a decision.")
            time.sleep(5)
            save_game()
            chapter_8()
            return
    else:
        print("Invalid choice. You continue down the path without making a decision.")
        time.sleep(5)
        save_game()
        chapter_8()
        return
        #This moves to the next chapter

def chapter_8():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_8"
    print("***************************\n"
          "Chapter 8: The Fire Dungeon\n"
          "***************************\n")
    time.sleep(2)
    print(DUNGEON_3)
    time.sleep(2)
    print(f"You and {COMPANION} arrive at the entrance of the fire dungeon,"
          "a dark cave filled with molten lava and fire.")
    time.sleep(5)
    print("The heat is intense, and you can feel the sweat pouring down your face.")
    time.sleep(5)
    print(f"Be careful. This place is known for its lava creatures :{COMPANION}")
    time.sleep(5)
    print("You nod and start to explore the dungeon, searching for the key.")
    time.sleep(5)
    print("As you venture deeper, you come across a large underground chamber filled with lava.")
    time.sleep(5)
    print("In the center of the chamber, you see a small island with a pedestal on it.")
    time.sleep(5)
    print("On the pedestal, you can see a glowing red key.")
    time.sleep(5)
    print(f"You and {COMPANION} realize that this must be the third key you are looking for.")
    time.sleep(5)
    print("Before either of you could react, a giant beast emerges from the lava,"
          "its eyes glowing with a menacing light.")
    time.sleep(5)
    print("The beast is a massive fire phoenix, its body made of pure flame.")
    time.sleep(5)
    print("****************************\n"
          "  flame The Beast of Fire \n"
          "****************************\n")
    print(FLAME)
    # This prints the ascii art for flame
    # Dragon choice is used as flame was originally a dragon
    # but was changed to a phoenix mid way through
    time.sleep(5)
    phoenix_choice = input("flame starts charging up it's attack! (Attack/Dodge): ")
    time.sleep(5)
    decrease_health()
    time.sleep(5)
    if phoenix_choice.lower() == "attack":
        print("flame breathes fire at you, before either of " \
              "you could attack scorching your skin and leaving you in pain.")
        time.sleep(5)
        decrease_health()
        print(f"{COMPANION}'s health is low")
        time.sleep(5)
        print(f"You and {COMPANION} are both injured and need to"
              "find a way to defeat flame before it attacks again.")
        time.sleep(5)
        phoenix_choice2 = input("You can either type 'Attack' to attack"
                                f"flame or type 'Heal' to heal yourself and {COMPANION}: ")
        if phoenix_choice2.lower() == "attack":
            print(f"You and {COMPANION} attack flame with all your might,"
                  "striking it with your weapons.")
            time.sleep(5)
            print("flame roars in pain, but it is not defeated yet.")
            time.sleep(5)
            phoenix_choice3 = input("Type 'Attack' to attack flame again or"
                                    f"type 'Heal' to heal yourself and {COMPANION}: ")
            while True:
            #A loop is used to allow the PLAYER to restart at select points
                if phoenix_choice3.lower() == "attack":
                    print(f"You and {COMPANION} attack flame with all your might.")
                    time.sleep(5)
                    print("flame roars in pain, but it is not defeated yet.")
                    time.sleep(5)
                    print("flame spews out lava, and melts you and COMPANION")
                    time.sleep(5)
                    death()
                    break
                #This kills the PLAYER
                elif phoenix_choice3.lower() == "heal":
                    print(f"You use a healing potion to heal yourself and {COMPANION}.")
                    increase_health(50)
                    time.sleep(5)
                    print(f"{COMPANION} is back in the fight!")
                    time.sleep(5)
                    print("You both attack flame together, striking it with all your might.")
                    time.sleep(5)
                    print("flame roars in pain, it's hardened feathers are " \
                          "starting to crack under your combined assault.")
                    phoenix_choice4 = input("Type 'Attack' to attack flame again or"
                                            f"type 'Heal' to heal yourself and {COMPANION}: ")
                    if phoenix_choice4.lower() == "attack":
                        print(f"You and {COMPANION} attack flame's core"
                              "with all your might, striking it with your weapons.")
                        time.sleep(5)
                        print("flame roars in pain, and it crumbles to the ground, defeated.")
                        time.sleep(5)
                        print(f"You and {COMPANION} stand victorious,"
                              "breathing heavily from the intense battle.")
                        time.sleep(5)
                        print("You search the dragon's remains and find a glowing " \
                              "red key that unlocks a hidden door in the dungeon.")
                        time.sleep(5)
                        print(f"You and {COMPANION} enter the hidden door,"
                              "hoping to find the next key inside.")
                        time.sleep(5)
                        print("As you step through the door, you find yourselves "
                              "in a dimly lit chamber filled with ancient artifacts.")
                        time.sleep(5)
                        print("In the center of the room, you see a pedestal with a " \
                              "glowing red key.")
                        time.sleep(5)
                        print("****************************\n"
                               "  3 Key Achieved 2 left. \n"
                              "****************************\n")
                        save_game()
                        time.sleep(5)
                        dark_sword_story()
                        time.sleep(5)
                        chapter_9()
                        break
                #This shows the sword upgrade story
                #This moves to the next chapter
                elif phoenix_choice3.lower() == "heal":
                    print(f"You use a healing potion to heal yourself and {COMPANION}.")
                    time.sleep(5)
                    print(f"{COMPANION} is back in the fight!")
                    time.sleep(5)
                    print("flame attacks you before you can attack again!")
                    time.sleep(5)
                    print(f"You and {COMPANION} are both injured and"
                          "need to find a way to defeat flame before it attacks again.")
                    decrease_health(50)
                    time.sleep(5)
                    print(f"{COMPANION}'s health is low")
                    time.sleep(5)
                    print("flame attacks you before you can attack again!")
                    death()
                    return
                #This kills the PLAYER
                else:
                    print("Invalid choice. flame attacks you again!")
                    death()
                    return
                #This kills the PLAYER since they didn't provide an appropriate response
        elif phoenix_choice2.lower() == "heal":
            print(f"You use a healing potion to heal yourself and {COMPANION}.")
            increase_health(50)
            time.sleep(5)
            print(f"{COMPANION} is back in the fight!")
            time.sleep(5)
            print("You both attack flame together, striking it with all your might.")
            time.sleep(5)
            print("flame roars in pain, but it's feathers harden under your combined assault")
            time.sleep(5)
            print("flame attacks you before you can attack again!")
            time.sleep(5)
            print("flame charges up another burst of fire,"
                  f"and spews directly at you and {COMPANION}")
            time.sleep(5)
            death()
            return
            #This kills the PLAYER
        else:
            print(f"Invalid option, flame spews hot lava all over you and {COMPANION}.")
            time.sleep(5)
            death()
            return
        #This kills the PLAYER as they entered the wrong input
    elif phoenix_choice.lower() == "dodge":
        print("You quickly dodge flame's attack, narrowly avoiding its powerful strike.")
        time.sleep(5)
        print("You counterattack, striking flame with all your might.")
        time.sleep(5)
        print("The phoenix staggers back, but it is not defeated yet."
              f"You and {COMPANION} must work together to defeat it.")
        time.sleep(5)
        while True:
            phoenix_choice5 = input("You can either type 'Attack' to attack"
                                    "flame again or type 'Heal' to heal"
                                    f"yourself and {COMPANION}: ")
            if phoenix_choice5.lower() == "attack":
                print(f"You and {COMPANION} attack flame with all your might.")
                time.sleep(5)
                print(f"You and {COMPANION} attack flame's core with all your might,"
                      "striking it with your weapons.")
                time.sleep(5)
                print("flame roars in pain, and it crumbles to the ground, defeated.")
                time.sleep(5)
                print(f"You and {COMPANION} stand victorious,"
                      "breathing heavily from the intense battle.")
                time.sleep(5)
                print("You search the dragon's remains and find a " \
                      "glowing red key that unlocks a hidden door in the dungeon.")
                time.sleep(5)
                print(f"You and {COMPANION} enter the hidden door,"
                      "hoping to find the next key inside.")
                time.sleep(5)
                print("As you step through the door, " \
                      "you find yourselves in a dimly lit chamber filled with ancient artifacts.")
                time.sleep(5)
                print("In the center of the room, you see a pedestal with a glowing red key.")
                time.sleep(5)
                print("****************************\n"
                       "  3 Key Achieved 2 left. \n"
                      "****************************\n")
                save_game()
                time.sleep(5)
                dark_sword_story()
                #Displays the sword upgrade story
                time.sleep(5)
                chapter_9()
                break
            #This shows the sword upgrade story
            elif phoenix_choice5.lower() == "heal":
                print(f"You use a healing potion to heal yourself and {COMPANION}")
                time.sleep(5)
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
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_9"
    print('***************************\n'
    "Chapter 9: The Path to the Ice Dungeon\n"
          '***************************\n')
    time.sleep(2)
    print(f"You and {COMPANION} exit the fire dungeon and continue down a path,"
          "the heat giving way to a more relaxed meadow atmosphere.")
    time.sleep(5)
    print("You spot a small village in the distance, and you can decide " \
          "to stop there to rest and gather supplies.")
    time.sleep(5)
    print(SMALL_VILLAGE)
    time.sleep(5)
    village_choice = input("Do you want to stop at the village? (Yes/No): ")
    if village_choice.lower() == "yes":
        print(f"You and {COMPANION} decide to stop at the village.")
        time.sleep(5)
        print("Before you you approach the villagers, you notice a " \
              "small shop selling potions and supplies.")
        time.sleep(5)
        print("You decide to enter the shop and see what they have to offer.")
        time.sleep(5)
        print(f"{COMPANION} says, 'Hello, shopkeeper!"
              "Do you have any potions or supplies that could help us on our journey?'")
        time.sleep(5)
        print("The shopkeeper nods and shows you a selection of potions and supplies.")
        time.sleep(5)
        print("Maps, healing potions, and other useful items are available "
              "for purchase but one item catches your eye.")
        time.sleep(5)
        print("A dusty old map that seems to lead to the next dungeon.")
        time.sleep(5)
        print("You ask the shopkeeper about the map, and he tells you that it "
              "is a rare find, but he is willing to sell it to you for a fair price.")
        map_choice = input("You can buy a map for 20 gold coins. Do you want to buy it? (Yes/No): ")
        #User input is stored as mapchoice
        if map_choice.lower() == "yes":
            print(f"You buy the map and give to {COMPANION} to analyze")
            time.sleep(5)
            decrease_gold(20)
            time.sleep(5)
            save_game()
            time.sleep(5)
            village()
            return
        #This stops at the village after buying the map
        else:
            print("You decide not to buy the map and continue down the path without it.")
            time.sleep(5)
            save_game()
            time.sleep(5)
            village()
            return
        #This stops at the village without buying
    elif village_choice.lower() == "no":
        print(f"You and {COMPANION} decide to continue down the path"
              "without stopping at the village.")
        time.sleep(5)
        save_game()
        time.sleep(5)
        save_game()
        time.sleep(5)
        chapter_9part2()
        return
    #This skips the village without reseting health and faces the boss without a full health bar
    else:
        print("Invalid choice. You continue down the path without stopping at the village.")
        time.sleep(5)
        save_game()
        time.sleep(5)
        save_game()
        time.sleep(5)
        chapter_9part2()
        return
    #This is for invalid input

def village():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "village"
    print("As you enter the village, you are greeted by friendly " \
          "villagers who offer you food and shelter.")
    time.sleep(5)
    print("This is a nice place to rest and"
          f"gather supplies before we continue our journey. :{COMPANION}")
    time.sleep(5)
    print("You spend some time in the village, " \
          "resting and preparing for the next part of your journey.")
    time.sleep(5)
    reset_health()
    print("You feel refreshed and ready to continue your journey.")
    time.sleep(5)
    print("You thank the villagers for their hospitality and prepare to leave the village.")
    time.sleep(5)
    save_game()
    time.sleep(5)
    chapter_9part2()
#This is for the village bit which resets the PLAYERs health and sets a checkpoint

def chapter_9part2():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_9part2"
    print("***************************\n"
     "Chapter 9 Part 2: The Journey Continues\n"
          "***************************\n")
    time.sleep(2)
    print(f"You and {COMPANION} follow the map's directions, navigating through the mountains.")
    time.sleep(5)
    print(DUNGEON_4)
    time.sleep(5)
    print("After a long journey, you arrive at a crossroad.")
    time.sleep(5)
    print(f"{COMPANION} says, 'Where do we go now?'")
    crossroad_choice = input("Do you want to go left (snowy mountains) "
                             "or right (icy cave)? (Left/Right): ")
    match crossroad_choice.lower().strip():
        case "left":
            print(f"You and {COMPANION} decide to go left towards the snowy mountains.")
            time.sleep(5)
            print("The temperature drops and you can see your breath in the cold air.")
            time.sleep(5)
            print(f"{COMPANION} says, 'We must be close to the ice dungeon.'")
            time.sleep(5)
            print("As you continue, the ground shakes and you are buried under a pile of snow.")
            death()
        #death due to avalanche
        case "right":
            print(f"You and {COMPANION} decide to go right towards the icy cave.")
            time.sleep(5)
            print("Entering the cave, the temperature drops further "
                  "and icicles hang from the ceiling.")
            time.sleep(5)
            print(f"This must be the ice dungeon. We need to be careful. :{COMPANION}")
            time.sleep(5)
            print("You explore the cave and find a locked underground chamber; " \
                  "you need a key to open it.")
            time.sleep(5)
            print(f"We must find the key to unlock this door. :{COMPANION}")
            time.sleep(5)
            print("Searching the chamber, you discover 2 small chests hidden behind a pile of ice.")
            time.sleep(5)
        #No death
            ice_chest_choice = input("Do you want to open the left chest "
                                     "or the right chest? (Left/Right): ")
            while True:
                match ice_chest_choice.lower().strip():
                    case "left":
                        print("You open the left chest and find a shiny key inside!")
                        time.sleep(5)
                        print(f"This must be the door key! :{COMPANION}")
                        time.sleep(5)
                        print("You insert the key into the lock and " \
                              "the door creaks open, revealing the next part of the dungeon.")
                        time.sleep(5)
                        print(f"You and {COMPANION} step through, ready for further challenges.")
                        time.sleep(5)
                        print("An icicle hits you on the head, and you black out.")
                        time.sleep(5)
                        print("When you wake up, you're in a giant icy cavern"
                              f"and {COMPANION} is missing as well as your sword.")
                        time.sleep(5)
                        print("A dirty rag in the corner starts moving, "
                              "and a ghoulish creature emerges.")
                        time.sleep(5)
                        print("*****************************\n"
                                  "Morjun the Ice wraith\n"
                              "*****************************\n")
                        time.sleep(5)
                        print(WRAITH)
                        time.sleep(5)
                        print("Morjun lunges at you, slashing with icy claws.")
                        time.sleep(5)
                        decrease_health()
                        time.sleep(5)
                        print("Stumbling back, you notice a rusty sword nearby.")
                        time.sleep(5)
                        wraith_choice = input("Do you want to pick up the sword and " \
                                              "fight Morjun or try to escape " \
                                              "the cavern? (Fight/Escape): ")
                        match wraith_choice.lower().strip():
                            case "fight":
                                print("You pick up the sword and prepare to fight Morjun.")
                                time.sleep(5)
                                print("You dodge Morjun's attack and strike, " \
                                      "hitting it in the side.")
                                time.sleep(5)
                                while True:
                                    wraith_choice2 = input("Do you want to attack again "
                                                           "or heal yourself? (Attack/Heal): ")
                                    match wraith_choice2.lower().strip():
                                        case "attack":
                                            print("You attack Morjun with all your might, "
                                                  "and it falls to the ground, defeated.")
                                            time.sleep(5)
                                            print("You search Morjun's remains and " \
                                                  "find a glowing ice key that unlocks a door.")
                                            time.sleep(5)
                                            print(f"You open a door and spot {COMPANION}"
                                                    "in a cage.")
                                            time.sleep(5)
                                            print(f"You free {COMPANION} from the cage and carry"
                                                  "them out of the cavern.")
                                            time.sleep(5)
                                            print(f"You and {COMPANION} step out of the cavern"
                                                  "through another door into a dimly lit maze.")
                                            time.sleep(5)
                                            maze_choice = input("Would you like to explore " \
                                                                "the maze or return to the cavern? "
                                                                "(Explore/Return): ")
                                            match maze_choice.lower().strip():
                                                case "explore":
                                                    print(f"You and {COMPANION} decide to explore"
                                                          "the maze for a way out.")
                                                    time.sleep(5)
                                                    maze_choice2 = input("Do you want to go" \
                                                                         "left or right? "
                                                                         "(Left/Right): ")
                                                    match maze_choice2.lower().strip():
                                                        case "left":
                                                            print("You take the left path "
                                                                  "and find a " \
                                                                  "small clearing.")
                                                            time.sleep(5)
                                                            print("In the clearing, a pedestal " \
                                                                  "holds a glowing ice key.")
                                                            time.sleep(5)
                                                            print("****************************\n"
                                                                     "4 Key Achieved 1 left.\n"
                                                                  "****************************\n")
                                                            time.sleep(5)
                                                            save_game()
                                                            time.sleep(5)
                                                            chapter_10()
                                                            break
                                                    #Achieves key and continues to next chapter
                                                        case "right":
                                                            print("You take the right path and end"
                                                                  "in a dead end. Go back!")
                                                            time.sleep(5)
                                                    #Repeats until they choose left
                                                        case _:
                                                            print("Invalid choice. " \
                                                                  "Returning to cavern.")
                                                            time.sleep(5)
                                                            return
                                                    #Goes back to question
                                                case "return":
                                                    print(f"You and {COMPANION}"
                                                          "return to the cavern.")
                                            #Goes back to cavern and repeats
                                                case _:
                                                    print("Invalid choice. Returning to cavern.")
                                                    time.sleep(5)
                                                    return
                                            #Goes back to cavern and repeats
                                        case "heal":
                                            print("You use a healing potion to heal yourself.")
                                            time.sleep(5)
                                            increase_health(50)
                                            time.sleep(5)
                                            print("Unfortunately, you trip and fall leaving " \
                                                  "you in the cave forever.")
                                            time.sleep(5)
                                            death()
                                            return
                                        #death
                                        case _:
                                            print("Invalid choice.")
                                            break
                                    #Repeats the question
                            case "escape":
                                print("You try escaping but Morjun possesses you.")
                                time.sleep(5)
                                death()
                                return
                            #death
                            case _:
                                print("Invalid choice. You trip over a rock.")
                                time.sleep(5)
                                death()
                                return
                            #Gets killed by a rock
                    case "right":
                        print("You open the right chest and find a pile of gold coins.")
                        time.sleep(5)
                        increase_gold(50)
                        time.sleep(5)
                        print(f"Nice find, but we still need the key. :{COMPANION}")
                        time.sleep(5)
                        #Collects coins then loops the question
                    case _:
                        print("Choose a valid option")
                     #Loops the question
        case _:
            print("Invalid choice. Choose again.")
            time.sleep(5)
        #Loops


def chapter_10():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_10"
    print("***************************\n"
    "Chapter 10: The Path to the Final Dungeon\n"
          "***************************\n")
    time.sleep(2)
    print(f"You and {COMPANION} exit the ice dungeon and continue towards the last dungeon,"
          "the icy terrain giving way to rocky cliffs.")
    time.sleep(5)
    print("The air grows colder, and you can see your breath in the frigid air.")
    time.sleep(5)
    print("The final key is said to be hidden in a dark dungeon,"
          f"deep within the mountains according to the map. :{COMPANION}")
    time.sleep(5)
    print("You nod in agreement, determined to find the final key and rescue the princess.")
    time.sleep(5)
    print("As you continue down the path, you come across a group of trolls blocking your way.")
    time.sleep(5)
    print(TROLL)
    time.sleep(5)
    print("The trolls are armed with large clubs and look ready for a fight.")
    time.sleep(5)
    print(f"{COMPANION} whispers, 'We need to be careful."
          "The trolls are known for their brute"
          "strength and cunning traps.'")
    time.sleep(5)
    troll_choice = input("Do you want to fight the trolls or try " \
                         "to reason with them? (Fight/Reason): ")
    if troll_choice.lower() == "fight":
        print(f"You and {COMPANION} charge at the trolls, weapons drawn.")
        time.sleep(5)
        print(f"The trolls fight back fiercely, but you and {COMPANION}"
              "are able to defeat them after a tough battle.")
        time.sleep(5)
        print("You search the trolls' remains and find a map that leads to the final dungeon.")
        time.sleep(5)
        print(f"You and {COMPANION} take the map and prepare to continue your journey.")
        time.sleep(5)
        save_game()
        time.sleep(5)
        chapter_11()
        time.sleep(5)
    #Continues to next chapter
    elif troll_choice.lower() == "reason":
        print("You try to reason with the trolls, explaining that you " \
              "mean no harm and are only looking for the final key.")
        time.sleep(5)
        print("The trolls try listening to your words, yet they don't speak English.")
        time.sleep(5)
        death()
        return
    #death due to language barrier

def chapter_11():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_11"
    print("***************************\n"
          "Chapter 11: The Final Dungeon\n"
          "***************************\n")
    print(f"You and {COMPANION} arrive at the entrance of the final dungeon,"
          "a dark cave filled with ominous shadows.")
    time.sleep(5)
    print(DUNGEON_5)
    time.sleep(5)
    print("The air is thick with tension, and you can feel the weight of " \
          "the final challenge ahead.")
    time.sleep(5)
    print("This is it. The final key is said to"
          f"be hidden in this dungeon, guarded by a powerful monster. :{COMPANION}")
    time.sleep(5)
    print("You nod, determined to find the final key and rescue the princess.")
    time.sleep(5)
    print("As you venture deeper into the dungeon, you come across " \
          "a large underground chamber filled with darkness.")
    time.sleep(5)
    print("In the center of the chamber, you see a pedestal with a glowing black key.")
    time.sleep(5)
    print("But before you can approach the pedestal, a massive " \
          "shadowy figure emerges from the darkness.")
    time.sleep(5)
    print("The figure is a giant shadow beast, its eyes glowing with a menacing light.")
    time.sleep(5)
    print("****************************\n"
            "  Desbio the Dark Beast \n"
          "****************************\n")
    time.sleep(5)
    print(DESBIO)
    #Prints ascii for boss
    time.sleep(5)
    beast_choice = input("Before either of you could move, " \
                         "Desbio strikes you both in the back, (Attack/Dodge): ")
    time.sleep(5)
    decrease_health()
    time.sleep(5)
    if beast_choice.lower() == "attack":
        print("Desbio lunges at you, its claws slashing through the air.")
        time.sleep(5)
        decrease_health()
        #Lowers health randomly
        print(f"{COMPANION}'s health is low")
        time.sleep(5)
        print(f"You and {COMPANION} are both injured and need to find a way"
              "to defeat desbio before it attacks again.")
        time.sleep(5)
        beast_choice2 = input("You can either type 'Attack' to attack desbio or"
                              f"type 'Heal' to heal yourself and {COMPANION} (Attack/Heal): ")
        if beast_choice2.lower() == "attack":
            print(f"You and {COMPANION} attack desbio with all your might,"
                  "striking it with your weapons.")
            time.sleep(5)
            print("Desbio roars in pain, but it is not defeated yet.")
            time.sleep(5)
            beast_choice3 = input("Type 'Attack' to attack desbio again or"
                                  f"type 'Heal' to heal yourself and {COMPANION} (Attack/Heal): ")
            while True:
            #These are for loops
                if beast_choice3.lower() == "attack":
                    print(f"You and {COMPANION} attack desbio with all your might.")
                    time.sleep(5)
                    print("Desbio roars in pain, but it is not defeated yet.")
                    time.sleep(5)
                    print("You realize that you need to find a way to " \
                          "weaken it before you can defeat it.")
                    time.sleep(5)
                elif beast_choice3.lower() == "heal":
                    print(f"You use a healing potion to heal yourself and {COMPANION}.")
                    increase_health(50)
                    #Increases health
                    time.sleep(5)
                    print(f"{COMPANION} is back in the fight!")
                    time.sleep(5)
                    print("You both attack desbio together, striking it with all your might.")
                    time.sleep(5)
                    print("Desbio roars in pain, it's scales are starting to " \
                          "crack under your combined assault.")
                    time.sleep(5)
                    beast_choice4 = input("Type 'Attack' to attack desbio"
                                         "again or type 'Heal' to heal"
                                         f"yourself and {COMPANION} (Attack/Heal): ")
                    if beast_choice4.lower() == "attack":
                        print(f"You and {COMPANION} attack desbio's core"
                              "with all your might, striking it with your weapons.")
                        time.sleep(5)
                        print("Desbio roars in pain, and it crumbles to the ground, defeated.")
                        time.sleep(5)
                        print(f"You and {COMPANION} stand victorious, breathing"
                              "heavily from the intense battle.")
                        time.sleep(5)
                        print("You search the beast's remains and find a " \
                              "glowing black key that unlocks a hidden door in the dungeon.")
                        time.sleep(5)
                        print(f"You and {COMPANION} enter the hidden door,"
                              "hoping to find the princess inside.")
                        time.sleep(5)
                        print("As you step through the door, you find yourselves "
                              "in a dimly lit chamber filled with ancient artifacts.")
                        time.sleep(5)
                        print("In the center of the room, you see a pedestal " \
                              "with a glowing black key.")
                        time.sleep(5)
                        print("****************************\n"
                             "  5 Keys Achieved None left. \n"
                              "****************************\n")
                        print("You take the key and prepare to rescue the princess.")
                        time.sleep(5)
                        save_game()
                        dark_shield_story()
                        time.sleep(5)
                        chapter_12()
                        return
                        #Shows the shield upgrade story and continues
                    elif beast_choice4.lower() == "heal":
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
        elif beast_choice2.lower() == "heal":
            print(f"You use a healing potion to heal yourself and {COMPANION}.")
            time.sleep(5)
            increase_health(50)
            print(f"{COMPANION} is back in the fight!")
            time.sleep(5)
            print("Desbio attacks you before you can attack again!")
            time.sleep(5)
            print(f"You and {COMPANION} are both injured and need to"
                  "find a way to defeat desbio before it attacks again.")
            decrease_health(50)
            time.sleep(5)
            print(f"{COMPANION}'s health is low")
            time.sleep(5)
            print("Desbio attacks you before you can attack again!")
            death()
            return
        #death
        else:
            print("Invalid choice. desbio attacks you again!")
            death()
            return
        #death due to invalid option
    elif beast_choice.lower() == "dodge":
        print("You quickly dodge desbio's attack, narrowly avoiding its powerful strike.")
        time.sleep(5)
        print("You counterattack, striking desbio with all your might.")
        time.sleep(5)
        print("The beast staggers back, but it is not defeated yet."
              f"You and {COMPANION} must work together to defeat it.")
        time.sleep(5)
        while True:
            beast_choice5 = input("You can either type 'Attack' to"
                                  "attack desbio again or type 'Heal' to"
                                  f"heal yourself and {COMPANION} (Attack/Heal): ")
            if beast_choice5.lower() == "attack":
                print(f"You and {COMPANION} attack desbio with all your might.")
                time.sleep(5)
                print(f"You and {COMPANION} attack desbio's core"
                      "with all your might, striking it with your weapons.")
                time.sleep(5)
                print("Desbio roars in pain, and it crumbles to the ground, defeated.")
                time.sleep(5)
                print(f"You and {COMPANION} stand victorious,"
                      "breathing heavily from the intense battle.")
                time.sleep(5)
                print("You search the beast's remains and find a " \
                      "glowing black key that unlocks a hidden door in the dungeon.")
                time.sleep(5)
                print(f"You and {COMPANION} enter the hidden door,"
                      "hoping to find the princess inside.")
                time.sleep(5)
                print("As you step through the door, you find yourselves "
                      "in a dimly lit chamber filled with ancient artifacts.")
                time.sleep(5)
                print("In the center of the room, you see a pedestal with a glowing black key.")
                time.sleep(5)
                print("****************************\n"
                      "  5 Keys Achieved None left. \n"
                      "****************************\n")
                time.sleep(5)
                save_game()
                time.sleep(5)
                dark_shield_story()
                time.sleep(5)
                chapter_12()
                return
            #Shows the shield upgrade story and continues to the next chapter
            elif beast_choice5.lower() == "heal":
                print(f"You use a healing potion to heal yourself and {COMPANION}.")
                increase_health(50)
                time.sleep(5)
                print(f"{COMPANION} is back in the fight!")
                time.sleep(5)
                print("You both attack Desbio together, striking it with all your might.")
                time.sleep(5)
                print("Desbio roars in pain, but it's scales harden under your combined assault")
                time.sleep(5)
                print("Desbio attacks you before you can attack again!")
                time.sleep(5)
                print("Desbio charges up another burst of dark energy,"
                      f"and spews directly at you and {COMPANION}")
                time.sleep(5)
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
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_12"
    print("***************************\n"
      "Chapter 12: The Calm Before The Storm"
          "***************************\n")
    time.sleep(2)
    print(f"You and {COMPANION} continue down the path, now with no clue where to go...")
    time.sleep(5)
    print("I've heard rumours of the final"
          f"beast that captured the princess, but never the location... :{COMPANION}")
    time.sleep(5)
    print("We may need to camp near a village for a few days as"
          f"I try to gather some info, I'm also quite tired... :{COMPANION}")
    time.sleep(5)
    print(f"Wait {USERNAME}!, I see another village"
          f"over the in the horizon. Let's go! :{COMPANION}")
    time.sleep(5)
    print(f"You and {COMPANION} approach the village, but it looks off...")
    time.sleep(5)
    print(ABANDONED_VILLAGE)
    time.sleep(5)
    print("There are no villagers in sight, it was abandoned quite " \
          "a few months ago by the looks of it...")
    time.sleep(5)
    abandoned_village_choice = input("Would you like to stay or " \
                                     "leave to find another village? (Stay/Leave): ")
    if abandoned_village_choice.lower() == "stay":
        print(f"Ok, {USERNAME} let's stay, we can gather info later! :{COMPANION}")
        chapter_12part2()
        return
    #Continues to the next chapter
    else:
        print(f"Ok, let's go, I'm kinda tired though... :{COMPANION}")
        time.sleep(5)
        print("You both travel along the path and reach a river...")
        time.sleep(5)
        print("You have no choice but to go back towards the village.")
        time.sleep(5)
        print("You arrived back at the village and sat down")
        chapter_12part2()
        time.sleep(5)
        return
    #Continues to next chapter and returns to the village

def chapter_12part2():
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_12part2"
    print(f"{COMPANION} approaches one of the abandoned houses and pulls out some goods")
    time.sleep(5)
    print(f"You set up the fire! :{COMPANION}")
    time.sleep(5)
    print("You oblige and went to go get firewood nearby")
    time.sleep(5)
    stick1 = input("Under a tree you find a piece. Type 'One' to pick up: ")
    if stick1.lower() == "one":
        print("Collected")
        #This shows the collecting stick sequence
    else:
        print("Not collected")
    stick2 = input("Under a piece of bark you find a piece. Type 'Two' to pick up: ")
    if stick2.lower() == "two":
        print("Collected")
    else:
        print("Not collected")
    stick3 = input("Near the camp you find a piece. Type 'Three' to pick up: ")
    if stick3.lower() == "three":
        print("Collected")
    else:
        print("Not collected")
    stick4 = input("Near a tree you find a piece. Type 'Four' to pick up: ")
    if stick4.lower() == "four":
        print("Collected")
    else:
        print("Not collected")
    stick5 = input("Under a leaf you find a piece. Type 'Five' to pick up: ")
    if stick5.lower() == "five":
        print("Collected all 5")
    else:
        print("Not collected")
    print("You return to the camp carrying all the wood...")
    time.sleep(5)
    print(f"{COMPANION} appears around a corner carrying a stack of books and yells at you")
    time.sleep(5)
    print(f"Come here {USERNAME} :{COMPANION}")
    time.sleep(5)
    print("I've analyzed the keys."
          "I believe the final creature could be dungeon somewhere underneath Fargon,"
          f"potentially underneath the capital :{COMPANION}")
    time.sleep(5)
    print("The capital? You ask")
    time.sleep(5)
    print("Yeah, according to this book,"
          f"there's a city called the capital located somewhere around here... :{COMPANION}")
    time.sleep(5)
    print("It's guarded by a forcefield, with 5 ancient machines guarding it")
    time.sleep(5)
    print("We should go find it, huh? Sounds like the princess could be located there!")
    time.sleep(5)
    print(f"You and {COMPANION} rest the night and leave tomorrow")
    time.sleep(5)
    print(f"You and {COMPANION} sleep the night")
    time.sleep(10)
    reset_health()
    chapter_13()
    #This resets the PLAYERs health to 100 and continues to the next chapter

def chapter_13():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_13"
    print("***************************\n"
            "Chapter 13: The capital"
          "***************************\n")
    time.sleep(2)
    print(f"You and {COMPANION} set off from the abandoned village...")
    time.sleep(5)
    print(f"Towards where {COMPANION} thinks where the capital is...")
    time.sleep(5)
    print(f"You and {COMPANION} walk for days")
    time.sleep(6)
    reset_health()
    print(f"{COMPANION} looks around, 'We should be here' :{COMPANION}")
    time.sleep(5)
    print("What, you reply, there's nothing here")
    time.sleep(5)
    print("All of a sudden, the ground beneath began to shake and split open")
    time.sleep(5)
    print(f"You and {COMPANION} drop into the cavern below")
    time.sleep(5)
    decrease_health()
    time.sleep(5)
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
                time.sleep(5)
                print("You reach a dead end...")
                time.sleep(5)
                print("All of a sudden a skeleton attacks you from behind...")
                print(SKELETON)
                time.sleep(5)
                death()
                break
            case 2:
                print("You walk into the darkness of the tunnel...")
                time.sleep(5)
                print("In the end, you reach a fountain...")
                time.sleep(5)
                print("Your deadly thirsty and drank from the fountain...")
                time.sleep(5)
                print("The fountain water was poisoned.")
                death()
                break
            case 3:
                print("You walk into the darkness of the tunnel...")
                time.sleep(5)
                print(f"You notice, a shadow up ahead, it could be {COMPANION}...")
                time.sleep(5)
                print("You run towards the shadow...")
                time.sleep(5)
                print("You walk right past the shadow...")
                time.sleep(5)
                print(f"You arrive back at the village, alone, with no {COMPANION} in sight...")
                time.sleep(5)
                print("You died of loneliness and despair")
                time.sleep(5)
                death()
                break
            case 4:
                print("You walk into the darkness of the tunnel...")
                time.sleep(5)
                print(f"You notice a shadow up ahead, it could be {COMPANION}...")
                time.sleep(5)
                print(f"Hey, come {USERNAME}! :{COMPANION}")
                time.sleep(5)
                print("You run towards the shadow...")
                time.sleep(5)
                print(f"You arrive at {COMPANION} and hug them tightly")
                time.sleep(5)
                print(f"{COMPANION} says, 'I thought I lost you!'")
                time.sleep(5)
                print("You realise that there was a blue misty wall at the " \
                      "end of the tunnel blocking your way further...")
                time.sleep(5)
                print(f"You and {COMPANION} then spot another tunnel to the"
                      "right of the blue wall...")
                time.sleep(5)
                print(f"You and {COMPANION} walk down the tunnel, hoping to find to the capital")
                time.sleep(5)
                chapter_14()
                break
            #This goes to the next chapter
            case 5:
                print("You walk into the darkness of the tunnel...")
                time.sleep(5)
                print("You spot  a faint light in the distance...")
                time.sleep(5)
                print("You walk towards the light...")
                time.sleep(5)
                print("You arrive at a small campfire, with a note next to it...")
                time.sleep(5)
                print("The note reads: 'Beware of the final beast, " \
                      "it lurks in the shadows of the capital.'")
                time.sleep(5)
                print("You take the note and continue down the tunnel...")
                time.sleep(5)
                print("You arrive at a dead end, with no way out...")
                time.sleep(5)
                print("You sit down and wait for help...")
                time.sleep(5)
                print("After a few hours, you hear a voice calling your name...")
                time.sleep(5)
                print(f"It sounds like {COMPANION}, yet it doesn't!")
                time.sleep(5)
                print("You stand up and walk towards the voice...")
                time.sleep(5)
                print("You arrive at a small clearing, " \
                      "with a shadowy figure standing in the middle.")
                time.sleep(5)
                print("The figure is cloaked in darkness, its eyes glowing with a menacing light.")
                time.sleep(5)
                print("****************************\n"
                      "  The Shadowy Figure \n"
                      "****************************\n")
                time.sleep(5)
                print(MYSTERIOUS_CHARACTER)
                time.sleep(5)
                print("You have come far, but you will not find the princess here. " \
                      ":Mysterious Figure")
                time.sleep(5)
                print(f"You ask the figure where the princess and {COMPANION} is,"
                      "but it only laughs.")
                time.sleep(5)
                print("The figure lunges at you, its claws slashing through the air.")
                time.sleep(5)
                print("You try to dodge the attack, but the figure is too fast.")
                time.sleep(5)
                print(f"You've came far, yet this is where it ends for you, {USERNAME}.")
                time.sleep(5)
                print("The figure strikes you down, and you fall to the ground, defeated.")
                time.sleep(5)
                print("You hear the figure laugh as it disappears into the shadows.")
                time.sleep(5)
                print("This creature was not the final beast, " \
                      "but a mere shadow of what is to come.")
                time.sleep(5)
                death()
                break
            #This kills the PLAYER
            case _:
                print("Enter a valid number")
                return
            #This loops until the PLAYER enters a valid number

def chapter_14():
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_14"
    print("***************************\n"
          "Chapter 14: The First Machine\n"
          "***************************\n")
    time.sleep(2)
    print(f"You and {COMPANION} arrive at the first machine,"
          "a massive structure made of stone and metal.")
    time.sleep(5)
    print("The machine is covered in strange symbols and runes, "
          "and it seems to be powered by some kind of dark energy.")
    time.sleep(5)
    print(f"This must be one of the machines that guard the capital. :{COMPANION}")
    time.sleep(5)
    print("You nod in agreement, determined to find a way to disable the machine.")
    time.sleep(5)
    print("As you approach the machine, you notice a small" \
          "panel on the side with a glowing red button.")
    time.sleep(5)
    print(f"We need to find a way to activate this button. :{COMPANION}")
    time.sleep(5)
    print("You search the area around the machine and find a small lever hidden behind some rocks.")
    time.sleep(5)
    print("You pull the lever, and the machine comes to life, its gears " \
          "grinding and whirring as it powers up.")
    time.sleep(5)
    print("The glowing red button on the panel lights up, and you press it.")
    time.sleep(5)
    print("The machine shudders and shakes, and you can feel the ground beneath you tremble.")
    time.sleep(5)
    print("Suddenly, a massive door opens in the side of the machine, " \
          "revealing a dark chamber inside.")
    time.sleep(5)
    print(f"We need to go inside and see what we can find. :{COMPANION}")
    time.sleep(5)
    print(f"You and {COMPANION} enter the chamber, weapons drawn, ready for whatever lies ahead.")
    time.sleep(5)
    print("Inside the chamber, you find a series of strange machines "
          "and devices, all connected to a button on a pedestal in the center of the room.")
    time.sleep(5)
    print("You approach the pedestal and see that the button is glowing with a dark energy.")
    time.sleep(5)
    print("All of a sudden, you feel a strange urge " \
          "to press the button, as if it is calling to you.")
    time.sleep(5)
    print(f"We need to be careful. This could be a tra.. :{COMPANION}")
    time.sleep(5)
    print(f"But before {COMPANION} can finish their sentence, you press the button.")
    time.sleep(5)
    print("The machine shudders and shakes, and you can feel the ground beneath you tremble.")
    time.sleep(5)
    print("Suddenly, the machines in the room all spring to life, " \
          "their gears grinding and whirring as they power up.")
    time.sleep(5)
    print("You hear a loud rumbling noise, and the machines begin to open a trapdoor in the floor.")
    time.sleep(5)
    print(f"You and {COMPANION} look at each other, unsure of what to do next.")
    time.sleep(5)
    print("*****************************\n"
           "     The First guardian \n"
          "*****************************\n")
    time.sleep(5)
    guardian1()
#This goes to the first guardian fight

def guardian1():
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "guardian1"
    print("Suddenly, a massive mechanical guardian emerges from the trapdoor, " \
          "its eyes glowing with a menacing light.")
    time.sleep(5)
    print("The guardian is a towering figure made of metal and stone, " \
          "its body covered in intricate designs and runes.")
    time.sleep(5)
    print("It raises its massive fists, ready to attack.")
    time.sleep(5)
    print(f"You and {COMPANION} prepare for battle, your weapons drawn and ready to fight.")
    time.sleep(5)
    print("The guardian lunges at you, its fists swinging through the air.")
    time.sleep(5)
    print("You dodge the attack and strike back, hitting the guardian in the side.")
    time.sleep(5)
    print("The guardian roars in pain, but it is not defeated yet.")
    time.sleep(5)
    guardian_choice = input("Do you want to attack the guardian again or try " \
                            "to find a way to disable the machines? (Attack/Disable): ")
    if guardian_choice.lower() == "attack":
        print(f"You and {COMPANION} attack the guardian with all your might,"
              "striking it with your weapons.")
        time.sleep(5)
        print("The guardian roars in pain, but it is not defeated yet.")
        time.sleep(5)
        print("You realize that you need to find a way to disable " \
              "the machines before you can defeat the guardian.")
        time.sleep(5)
        disable_choice = input("Do you want to try to disable the machines "
                               "or keep attacking the guardian? (Disable/Attack): ")
        if disable_choice.lower() == "disable":
            print(f"You and {COMPANION} search the room for a way to disable the machines.")
            time.sleep(5)
            print("You find a control panel on the wall with a series of buttons and switches.")
            time.sleep(5)
            print("You quickly figure out how to disable the machines, "
                  "and they all shut down, leaving the guardian vulnerable.")
            time.sleep(5)
            print(f"You and {COMPANION} attack the guardian one last time,"
                  "striking it down and defeating it.")
            time.sleep(5)
            print("You search the guardian's remains and find a glowing red " \
                  "key that unlocks a hidden door in the machine.")
            time.sleep(5)
            print(f"You and {COMPANION} enter the hidden door,"
                  "hoping to find more clues about the final beast.")
            time.sleep(5)
            chapter_15()
        #This goes to chapter 15
        elif disable_choice.lower() == "attack":
            print(f"You and {COMPANION} keep attacking the guardian, but it is too strong.")
            time.sleep(5)
            print("The guardian strikes you down, and you fall to the ground, defeated.")
            time.sleep(5)
            death()
            return
        #death
        else:
            print("The guardian doesn't hesitate to attack back")
            death()
        #This kills the PLAYER due to invalid response
    elif guardian_choice.lower() == "disable":
        print(f"You and {COMPANION} search the room for a way to disable the machines.")
        time.sleep(5)
        print("You find a control panel on the wall with a series of buttons and switches.")
        time.sleep(5)
        print("You quickly figure out how to disable the machines, "
              "and they all shut down, leaving the guardian vulnerable.")
        time.sleep(5)
        print(f"You and {COMPANION} attack the guardian one last time,"
              "striking it down and defeating it.")
        time.sleep(5)
        print("You search the guardian's remains and find a glowing red key " \
              "that unlocks a hidden door in the machine.")
        time.sleep(5)
        print(f"You and {COMPANION} enter the hidden door, hoping to"
              "find more clues about the final beast.")
        time.sleep(5)
        chapter_15()
    #This goes to the nest chapter
    else:
        print("The guardian lumbers over towards you and crushes you")
        death()

def chapter_15():
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_15"
    print("***************************\n"
          "Chapter 15: The Second Machine\n"
          "***************************\n")
    time.sleep(2)
    print(f"You and {COMPANION} enter the second machine,"
          "a massive structure filled with gears and machinery.")
    time.sleep(5)
    print("The air is thick with the smell of rusty metal, "
          "and you can hear the sound of machinery whirring to life.")
    time.sleep(5)
    print("We need to find a way to"
          f"shut down this machine before it activates. :{COMPANION}")
    time.sleep(5)
    print("You nod in agreement, determined to stop the machine and find the final beast.")
    time.sleep(5)
    print("As you explore the machine, you come across a series of control panels and levers.")
    time.sleep(5)
    print("You quickly figure out how to disable the machine, and it begins to shut down.")
    time.sleep(5)
    print("But before you can celebrate, another massive mechanical " \
          "guardian emerges from the shadows, its eyes glowing with a menacing light.")
    time.sleep(5)
    print("The guardian is a towering figure made of metal and stone, " \
          "its body covered in intricate designs and runes.")
    time.sleep(5)
    print("It raises its massive fists, ready to attack.")
    time.sleep(5)
    print("****************************\n"
          "  The Second guardian \n"
          "****************************\n")
    time.sleep(5)
    guardian2()
#This goes to the next stage of the battle

def guardian2():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "guardian2"
    print("The guardian lunges at you, its fists swinging through the air.")
    time.sleep(5)
    print("You dodge the attack and strike back, hitting the guardian in the side.")
    time.sleep(5)
    print("The guardian roars in pain, but it is not defeated yet.")
    time.sleep(5)
    guardian_choice = input("Do you want to attack the guardian again or try " \
                            "to find a way to disable the machines? (Attack/Disable): ")
    if guardian_choice.lower() == "attack":
        print(f"You and {COMPANION} attack the guardian with all your might,"
              "striking it with your weapons.")
        time.sleep(5)
        print("The guardian roars in pain, but it is not defeated yet.")
        time.sleep(5)
        print("You realize that you need to find a way to disable the " \
              "machines before you can defeat the guardian.")
        time.sleep(5)
        disable_choice = input("Do you want to try to disable the machines "
                               "or keep attacking the guardian? (Disable/Attack): ")
        if disable_choice.lower() == "disable":
            print(f"You and {COMPANION} search the room for a way to disable the machines.")
            time.sleep(5)
            print("You find a control panel on the wall with a series of buttons and switches.")
            time.sleep(5)
            print("You quickly figure out how to disable the machines, "
                  "and they all shut down, leaving the guardian vulnerable.")
            time.sleep(5)
            print(f"You and {COMPANION} attack the guardian one last time,"
                  "striking it down and defeating it.")
            time.sleep(5)
            print("You search the guardian's remains and find a glowing " \
                  "blue key that unlocks a hidden door in the machine.")
            time.sleep(5)
            print(f"You and {COMPANION} enter the hidden door,"
                  "hoping to find more clues about the final beast.")
            time.sleep(5)
            final_machine()
        #Goes to next chapter
        elif disable_choice.lower() == "attack":
            print(f"You and {COMPANION} keep attacking the guardian, but it is too strong.")
            time.sleep(5)
            print("The guardian strikes you down, and you fall to the ground, defeated.")
            time.sleep(5)
            death()
        #kills the PLAYER
        else:
            print("The guardian suddenly stops moving")
            time.sleep(5)
            print(f"You and {COMPANION} stare bewildered")
            time.sleep(5)
            print("Suddenly, the guardian explodes")
            time.sleep(5)
            print("All those years being inactive and inside this humid room " \
                  "must have rusted something")
            death()
            return
    elif guardian_choice.lower() == "disable":
        print(f"You and {COMPANION} search the room for a way to disable the machines.")
        time.sleep(5)
        print("You find a control panel on the wall with a series of buttons and switches.")
        time.sleep(5)
        print("You quickly figure out how to disable the machines, "
              "and they all shut down, leaving the guardian vulnerable.")
        time.sleep(5)
        print(f"You and {COMPANION} attack the guardian one last time,"
              "striking it down and defeating it.")
        time.sleep(5)
        print("You search the guardian's remains and find a glowing " \
              "blue key that unlocks a hidden door in the machine.")
        time.sleep(5)
        print(f"You and {COMPANION} enter the hidden door,"
              "hoping to find more clues about the final beast.")
        time.sleep(5)
        final_machine()
    else:
        print("The guardian swings it huge arms at you")
        death()
        return
    #Goes to next chapter

def final_machine():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "final_machine"
    print("***************************\n"
          "Chapter 16: The Final Machine\n"
          "***************************\n")
    time.sleep(2)
    print(f"You and {COMPANION} enter the final machine,"
          "a massive structure filled with gears and machinery.")
    time.sleep(5)
    print("The air is thick with the smell of rusty metal, "
          "and you can hear the sound of machinery whirring to life.")
    time.sleep(5)
    print(f"This is it. The final machine that guards the capital. :{COMPANION}")
    time.sleep(5)
    print("You nod in agreement, determined to find a way to " \
          "shut down the machine and rescue the princess.")
    time.sleep(5)
    print("As you explore the machine, you come across a series of control panels and levers.")
    time.sleep(5)
    print("You quickly figure out how to disable the machine, and it begins to shut down.")
    time.sleep(5)
    print("You hear a loud rumbling noise, and the machines" \
          " begin to shut down the forcefield that surrounds the capital.")
    time.sleep(5)
    print(f"With the forcefield down, you and {COMPANION} rush out"
          "of the machine rooms and make your way to the heart of the capital.")
    chapter_16()
#This goes to the next chapter after disabling the forcefield

def chapter_16():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_16"
    print("***************************\n"
          "Chapter 16: The Final Showdown\n"
          "***************************\n")
    time.sleep(2)
    print(f"You and {COMPANION} enter the capital,"
          "a grand city filled with towering buildings and bustling streets.")
    time.sleep(5)
    print(NECRON)
    time.sleep(5)
    print("But something is off. The streets are eerily quiet, "
          "and you can feel a dark presence lurking in the shadows.")
    time.sleep(5)
    print(f"We need to find the final beast and rescue the princess. :{COMPANION}")
    time.sleep(5)
    print("You nod in agreement, determined to find the final beast and rescue the princess.")
    time.sleep(5)
    print("The grand architecture of the capital is breathtaking, " \
          "but the atmosphere is heavy with dread.")
    time.sleep(5)
    print("Gothic style buildings loom overhead, their windows dark and foreboding.")
    time.sleep(5)
    print("As you walk through the empty streets, you notice strange symbols " \
          "etched into the walls.")
    time.sleep(5)
    print("These symbols seem to pulse with a dark energy, "
          "and you can feel their power as you pass by.")
    time.sleep(5)
    print(f"{COMPANION} says, 'These symbols must be connected to the final beast.'")
    time.sleep(5)
    print(f"You and {COMPANION} continue to explore the capital,"
          "searching for any clues that might lead you to the final beast.")
    time.sleep(5)
    print("As you venture deeper into the capital, " \
          "you come across a large underground chamber filled with darkness " \
          "with a few crates inside.")
    time.sleep(5)
    print("In the center of the chamber, you see a pedestal with a glowing purple key.")
    time.sleep(5)
    print("But before you can approach the pedestal," \
          "a massive shadowy figure emerges from the darkness.")
    time.sleep(5)
    print("The figure is a giant shadow beast, its eyes glowing with a menacing light.")
    time.sleep(5)
    print("****************************\n"
    "   necron The Beast of Eternal Doom \n"
          "****************************\n")
    time.sleep(5)
    print(NECRON)
    time.sleep(5)
    save_game()
    necron_fight()
#This starts the boss fight

def necron_fight():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "Necron_fight"
    print("The beast lunges at you, its claws slashing through the air.")
    time.sleep(5)
    print("You dodge the attack and strike back, hitting the beast in the side.")
    time.sleep(5)
    print("Necron roars in pain, but it is not defeated yet.")
    time.sleep(5)
    necron_choice = input("Do you want to attack the beast again or heal? (Attack/Heal): ")
    if necron_choice.lower() == "attack":
        print(f"You and {COMPANION} attack the beast with all your might,"
              "striking it with your weapons.")
        time.sleep(5)
        print("The beast roars in pain, but it is not defeated yet.")
        time.sleep(5)
        print("Necron is too strong, and you realize that you need to find " \
              "a way to disable the machines before you can defeat it.")
        time.sleep(5)
        disable_choice = input("Do you want to try to disable the machines "
                               "or keep attacking the beast? (Heal/Attack): ")
        if disable_choice.lower() == "heal":
            print(f"You and {COMPANION} search the cavern for a way to heal yourselves.")
            time.sleep(5)
            print("You find a stash of healing potions and quickly use them " \
                  "to restore your health.")
            time.sleep(5)
            print("With your health restored, you feel ready to take on the beast again.")
            time.sleep(5)
            necron_fight2()
        #Goes to the second part of the fight
        elif disable_choice.lower() == "attack":
            print(f"You and {COMPANION} keep attacking the beast, but it is too strong.")
            time.sleep(5)
            print("The beast strikes you down, and you fall to the ground, defeated.")
            time.sleep(5)
            death()
        #Death
        else:
            print("Invalid choice. You continue to attack the beast without healing.")
            time.sleep(5)
            necron_fight2()
        #Goes to the second part of the fight without heal
    elif necron_choice.lower() == "heal":
        print(f"You and {COMPANION} search the cavern for a way to heal yourselves.")
        time.sleep(5)
        print("You find a stash of healing potions and quickly use them to restore your health.")
        time.sleep(5)
        print("With your health restored, you feel ready to take on the beast again.")
        time.sleep(5)
        necron_fight2()
    #Goees to second part of the fight
    else:
        print("Invalid choice. necron casts a dark spell, "
              "and you feel your strength draining away.")
        time.sleep(5)
        death()
        return
    #death

def necron_fight2():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "Necron_fight2"
    print("AHHHHHH, LIGHT WILL NEVER COME OVER THIS WORLD, " \
          "YOU CAN'T STOP ME YOU PUNY LITTLE INSECTS! necron yells")
    necron_choice2 = input("Do you want to attack the beast again or heal? (Attack/Heal): ")
    if necron_choice2.lower() == "attack":
        print(f"You and {COMPANION} attack the beast with all your might,"
              "striking it with your weapons.")
        time.sleep(5)
        print("The beast roars in pain, but it is not defeated yet.")
        time.sleep(5)
        print("Necron is too strong, and you realize that there are machines " \
              "surrounding the room healing necron, you need to find a way to " \
              "disable the machines before you can defeat it.")
        time.sleep(5)
        disable_choice2 = input("Do you want to try to disable the machines "
                                "or keep attacking the beast? (Disable/Attack): ")
        if disable_choice2.lower() == "disable":
            print(f"You and {COMPANION} search the cavern for a way to disable the machines.")
            time.sleep(5)
            print("You find a control panel on the wall with a series of " \
                  "buttons and switches and a book full of unknown letters.")
            time.sleep(5)
            print("You quickly flip through the book and find a passage " \
                  "that seems to describe the machines.")
            time.sleep(5)
            print("With this knowledge, you feel ready to take on the machines.")
            time.sleep(5)
            machines1()
        #Goes to next part
        elif disable_choice2.lower() == "attack":
            print(f"You and {COMPANION} keep attacking the beast, but it is too strong.")
            time.sleep(5)
            print("The beast strikes you down, and you fall to the ground, defeated.")
            time.sleep(5)
            death()
            return
        #death
        else:
            print("Necron suddenly slams into the cavern causing it to"
                  f"collapse on top of you and {COMPANION}")
            death()
            return
    elif necron_choice2.lower() == "heal":
        print(f"You and {COMPANION} search the cavern for a way to heal yourselves.")
        time.sleep(5)
        print("You find a stash of healing potions and quickly use them to restore your health.")
        time.sleep(5)
        print("With your health restored, you feel ready to take on the beast again.")
        time.sleep(5)
        necron_fight3()
    #Starts next sequence of the boss fight
    else:
        print(f"Necron summons a stack of playing cards on top of you and {COMPANION},"
              "crushing you both")
        death()
        return

def necron_fight3():
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "Necron_fight3"
    print("Necron roars in anger, its eyes glowing with a menacing light.")
    time.sleep(5)
    print("The beast lunges at you, its claws slashing through the air.")
    time.sleep(5)
    print("You dodge the attack and strike back, hitting the beast in the side.")
    time.sleep(5)
    print("Necron roars in pain, but it is not defeated yet.")
    time.sleep(5)
    necron_choice3 = input("Do you want to attack the beast again or " \
                           "destroy the machines? (Attack/Destroy): ")
    if necron_choice3.lower() == "attack":
        print(f"You and {COMPANION} attack the beast with all your might,"
              "striking it with your weapons.")
        time.sleep(5)
        print("The beast roars in pain, but it is not defeated yet.")
        time.sleep(5)
        print("Necron is too strong, and you realize that you need to find a " \
              "way to destroy the machines before you can defeat it.")
        time.sleep(5)
        destroy_choice = input("Do you want to try to destroy the machines "
                               "or keep attacking the beast? (Destroy/Attack): ")
        if destroy_choice.lower() == "destroy":
            print(f"You and {COMPANION} search the cavern for a way to destroy the machines.")
            time.sleep(5)
            print("You find a control panel on the wall with a series of " \
                  "buttons and switches and a book full of unknown letters.")
            time.sleep(5)
            print("You quickly flip through the book and find a passage " \
                  "that seems to describe the machines.")
            time.sleep(5)
            print("With this knowledge, you feel ready to take on the machines.")
            time.sleep(5)
            machines1()
        elif destroy_choice.lower() == "attack":
            print(f"You and {COMPANION} keep attacking the beast, but it is too strong.")
            time.sleep(5)
            print("The beast strikes you down, and you fall to the ground, defeated.")
            time.sleep(5)
            death()
        #Gets killed
        else:
            print(f"You and {COMPANION} look in dread as necron summons a hoard of goblins")
            time.sleep(5)
            print(f"The disoriented goblins start swarming you and {COMPANION}")
            time.sleep(5)
            death()
            return
    elif necron_choice3.lower() == "destroy":
        print("You search the cavern for a way to destroy the machines"
              f"while {COMPANION} distracts Necrom.")
        time.sleep(5)
        print("You find a control panel on the wall with a series of buttons "
              "and switches and a book full of unknown letters.")
        time.sleep(5)
        print("You quickly flip through the book and find a passage " \
              "that seems to describe the machines.")
        time.sleep(5)
        print("With this knowledge, you feel ready to take on the machines.")
        time.sleep(5)
        machines1()
    #Goes to the next chapter


def machines1():
    print("You spot the first machine, a massive structure made of stone and metal.")
    time.sleep(5)
    destroy1 = input("To destory it type (XYSDFBA): ")
    if destroy1.lower() == "xysdfba":
        print("You successfully destroy the first machine, and it crumbles to the ground.")
        time.sleep(5)
        print("You search the machine's remains and find a glowing " \
              "red key that unlocks a hidden door in the capital.")
        time.sleep(5)
        print(f"You and {COMPANION} enter the hidden door,"
              "hoping to find more clues about the final beast.")
        time.sleep(5)
        machines2()
    #Goes to next chapter
    else:
        print("You fail to destroy the first machine, and it remains intact.")
        time.sleep(5)
        print("You realize that you need to find a way to disable the " \
              "machine before you can proceed.")
        time.sleep(5)
        machines1()
    #Repeats

def machines2():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "machines2"
    print("You spot the second machine, a massive structure made of sharpened serpent scales.")
    time.sleep(5)
    destroy2 = input("To destroy it type (DNQEJJ): ")
    if destroy2.lower() == "dnqejj":
        print("You successfully destroy the second machine, and it crumbles to the ground.")
        time.sleep(5)
        print("You search the machine's remains and find a glowing " \
              "red key that unlocks a hidden door in the capital.")
        time.sleep(5)
        print(f"You and {COMPANION} enter the hidden door,"
              "hoping to find more clues about the final beast.")
        time.sleep(5)
        machines3()
    #Goes to next chapter
    else:
        print("You fail to destroy the second machine, and it remains intact.")
        time.sleep(5)
        print("You realize that you need to find a way to disable " \
              "the machine before you can proceed.")
        time.sleep(5)
        machines2()
    #Repeats

def machines3():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "machines3"
    print("You spot the third machine, a massive structure made of solidified lava.")
    time.sleep(5)
    destroy3 = input("To destroy it type (FNJREWNFJ): ")
    if destroy3.lower() == "fnjrewnfj":
        print("You successfully destroy the third machine, and it crumbles to the ground.")
        time.sleep(5)
        print("You search the machine's remains and find a glowing " \
              "red key that unlocks a hidden door in the capital.")
        time.sleep(5)
        print(f"You and {COMPANION} enter the hidden door,"
              "hoping to find more clues about the final beast.")
        time.sleep(5)
        machines4()
    #Goes to next chapter
    else:
        print("You fail to destroy the third machine, and it remains intact.")
        time.sleep(5)
        print("You realize that you need to find a way to disable " \
              "the machine before you can proceed.")
        time.sleep(5)
        machines3()
    #Repeats

def machines4():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "machines4"
    print("You spot the fourth machine, a massive structure made of pure packed ice.")
    time.sleep(5)
    destroy4 = input("To destroy it type (FNJQNRE): ")
    if destroy4.lower() == "fnjqnre":
        print("You successfully destroy the fourth machine, and it crumbles to the ground.")
        time.sleep(5)
        print("You search the machine's remains and find a glowing " \
              "red key that unlocks a hidden door in the capital.")
        time.sleep(5)
        print(f"You and {COMPANION} enter the hidden door,"
              "hoping to find more clues about the final beast.")
        time.sleep(5)
        machines5()
    #Goes to next chapter
    else:
        print("You fail to destroy the fourth machine, and it remains intact.")
        time.sleep(5)
        print("You realize that you need to find a way to disable " \
              "the machine before you can proceed.")
        time.sleep(5)
        machines4()
    #Repeats

def machines5():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "machines5"
    print("You spot the final machine, a massive structure made of pure refined darkness.")
    time.sleep(5)
    destroy5 = input("To destroy it type (JDEIJDU): ")
    if destroy5.lower() == "jdeijdu":
        print("You successfully destroy the fifth machine, and it crumbles to the ground.")
        time.sleep(5)
        print("Just in time, you turn around and see necron, the final beast, charging at you.")
        time.sleep(5)
        print(f"{COMPANION} is nowhere to be seen,"
              "and you realize that you are alone in this fight.")
        time.sleep(5)
        necron_fight4()
    #Goes to next part of the fight
    else:
        print("You fail to destroy the fifth machine, and it remains intact.")
        time.sleep(5)
        print("You realize that you need to find a way to disable " \
              "the machine before you can proceed.")
        time.sleep(5)
        machines5()
    #Repeats

def necron_fight4():
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "Necron_fight4"
    print("Necron roars in anger, its eyes glowing with a darker menacing light.")
    time.sleep(5)
    print("Necron shrieks another battle cry, "
          "and transforms into it's second form, a massive shadowy dragon.")
    time.sleep(5)
    print("*************************************\n"
"      necronom The Final Bringer of Eternal Darkness \n"
          "************************************\n")
    time.sleep(5)
    print(NECRON_SECOND_FORM)
    time.sleep(5)
    print("The dragon lunges at you, its claws slashing through the air.")
    time.sleep(5)
    print("You dodge the attack and strike back, hitting the dragon in the side.")
    time.sleep(5)
    print("Necronom roars in pain, but it is not defeated yet.")
    time.sleep(5)
    dragon_choice = input("Do you want to attack the dragon again or heal? (Attack/Heal): ")
    #Saves input as dragon_choice
    if dragon_choice.lower() == "attack":
        print(f"You and {COMPANION} attack the dragon with all your might,"
              "striking it with your weapons.")
        time.sleep(5)
        print("The dragon roars in pain, but it is not defeated yet.")
        time.sleep(5)
        print("Necronom is too strong, and yet you perservere through the pain "
              "and realize that inside one of the crates, is a book full of spells.")
        time.sleep(5)
        disable_choice = input("Do you want to try to cast a spell or" \
                               "keep attacking the dragon? (Cast/Attack): ")
        if disable_choice.lower() == "cast":
            print("You grab the book and quickly flip through the pages, " \
                  "searching for a spell that can help you defeat the dragon.")
            time.sleep(5)
            print(DARK_BOOK)
            time.sleep(5)
            print("You find a spell that seems to describe the dragon, "
                  "and you quickly memorize it.")
            time.sleep(5)
            print("Nazma incus draconis! you chant, and a burst of light erupts from your hands.")
            time.sleep(5)
            print("The dragon roars in pain, and you can see its " \
                  "scales begin to crack and crumble.")
            time.sleep(5)
            print("AHHHHHHHHHHHHHHHHHHHHHH, NOOOOOOOOOOOO! necronom screams  as it " \
                  "begins to disintegrate.")
            time.sleep(5)
            print("THIS WILL NOT BE THE END, THE PRINCESS IS NOT WHO SHE SEEMS, " \
                  "YOU WILL NEVER ESCAPE THIS PLACE ALIVE! necronom yells as " \
                  "it fades into the shadows.")
            time.sleep(5)
            print("You search the dragon's remains and find a glowing " \
                  "purple key that unlocks a hidden door in the chamber.")
            time.sleep(5)
            print(f"You and {COMPANION} enter the hidden door,"
                  "hoping to find more clues about the final beast.")
            time.sleep(5)
            companion_fight()
        #Continues to next chapter
        elif disable_choice.lower() == "attack":
            print(f"You and {COMPANION} keep attacking the dragon, but it is too strong.")
            time.sleep(5)
            print("The dragon strikes you down, and you fall to the ground, defeated.")
            time.sleep(5)
            death()
        #death
        else:
            print("Invalid choice. The dragon strikes you down, "
                  "and you fall to the ground, defeated.")
            time.sleep(5)
            death()
        #death due to invalid response
    elif dragon_choice.lower() == "heal":
        print("Necronom charges into you and picks you up high before dropping you")
        death()
    else:
        print("Necronom strikes you and COMPANION")
        death()


def companion_fight():
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "companion_fight"
    print("As you enter the hidden door, you find yourself in a " \
          "large chamber filled with darkness.")
    time.sleep(5)
    print("In the center of the chamber, you see a pedestal with a glowing purple key.")
    time.sleep(5)
    print("But before you can approach the pedestal, you hear a voice calling your name.")
    time.sleep(5)
    print(f"You turn around to look at {COMPANION} but he looks off")
    time.sleep(5)
    print("Their eyes are glowing with a dark energy.")
    time.sleep(5)
    print(f"{COMPANION} says, 'You have come far, but you will not find the princess here.'")
    time.sleep(5)
    print("The voice is distorted and twisted,"
          f"and you can feel a dark presence emanating from {COMPANION}.")
    time.sleep(5)
    print("****************************\n"
            "  Corrupted COMPANION \n"
          "****************************\n")
    time.sleep(5)
    print(f"You realize that {COMPANION} has been corrupted by"
          "the dark energy of necron, and you must fight them to save the princess.")
    time.sleep(5)
    companion_choice = input(f"Do you want to attack {COMPANION} or"
                             "try to reason with them? (Attack/Reason): ")
    if companion_choice.lower() == "reason":
        print(f"You try to reason with {COMPANION},"
              "but they are too far gone.")
        time.sleep(5)
        print(f"The corrupted {COMPANION} is strong,"
              "but you are determined to save them.")
        time.sleep(5)
        print(f"Too late, the corrupted {COMPANION} lunges at you,"
              "their claws slashing through the air.")
        time.sleep(5)
        print(f" {COMPANION} manages to strike you down,"
              "and you fall to the ground, defeated.")
        time.sleep(5)
        print(f"I'm sorry, {USERNAME}, but I cannot let you find the princess,"
              f"their voice distorted and twisted. :{COMPANION}")
        time.sleep(5)
        print(f"{COMPANION} leaves you lying on the ground, defeated,"
              "and walks away into the darkness.")
        time.sleep(5)
        print(f"You've made it far, but this is where it ends for you. :{COMPANION}")
        time.sleep(5)
        print(f"You hear the corrupted {COMPANION}"
              "laugh as they disappear into the shadows.")
        death()
        return
    elif companion_choice.lower() == "attack":
        print(f"You lunge at {COMPANION},"
              "your eyes filled with tears yet your heart filled with determination.")
        time.sleep(5)
        print(f"{COMPANION} tries to dodge your attack,"
              "but you manage to hit them in the side.")
        time.sleep(5)
        print(f"Wait, {USERNAME}, I can still be saved! "
              f"their voice filled with pain. :{COMPANION}")
        time.sleep(5)
        companion_choice2 = input(f"Would you like to continue attacking {COMPANION}"
                                  "or try to save them? (Attack/Save): ")
        time.sleep(5)
        if companion_choice2.lower() == "save":
            print("Fine, you reply")
            time.sleep(5)
            print(f"Thank you, {USERNAME}, I knew you would come to save me!"
                  f"their voice filled with hope. :{COMPANION}")
            time.sleep(5)
            print(f"You help {COMPANION} to their feet,"
                  "and they look at you with gratitude in their eyes.")
            time.sleep(5)
            print(f"'Come let's go, we need to get out of here', you say to {COMPANION}")
            time.sleep(5)
            print("We need to go find the princ...")
            time.sleep(5)
            print(f"{COMPANION} striked you in the bag,"
                  "their eyes glowing with a dark energy once again.")
            time.sleep(5)
            print("You really thought I was going to let you save me?"
                  f"{COMPANION} says, their voice distorted and twisted.")
            time.sleep(5)
            print(f"Bye bye, {USERNAME}, I hope you enjoy your"
                  f"stay in the darkness, {COMPANION} says with a sinister laugh.")
            death()
            return
        elif companion_choice2.lower() == "attack":
            print(f"You keep attacking {COMPANION},"
                  "determined to defeat them and save the princess.")
            time.sleep(5)
            print(f"The corrupted {COMPANION} fights back with all their might,"
                  "but you are relentless in your attack.")
            time.sleep(5)
            print("Finally, after a long and grueling battle,"
                  f"{COMPANION} surrenders.")
            time.sleep(5)
            print(f"Fine, I'm sorry, {USERNAME}, I didn't mean to hurt you,"
                  f"their voice filled with pain. :{COMPANION}")
            time.sleep(5)
            print("No, you replied, you were corrupted by the dark energy of necron, "
                   "and you must be stopped.")
            time.sleep(5)
            print(f"You hoist your sword towards {COMPANION},"
                  "ready to strike the final blow.")
            time.sleep(5)
            print("But before you can strike, you remember"
                  f"all the fond memories you had with {COMPANION}.")
            time.sleep(5)
            print("You remember the times you laughed together, " \
                  "the times you fought side by side, all the dungeons you faced together.")
            time.sleep(5)
            print(f"You realize that you cannot bring yourself to kill {COMPANION},"
                  "even if they corrupted, but yet he could still hurt you.")
            time.sleep(5)
            companion_choice3 = input(f"Do you want to spare {COMPANION} or"
                                      "finish them off? (Spare/Finish): ")
            if companion_choice3.lower() == "spare":
                print("You lower your sword, tears streaming down your face.")
                time.sleep(5)
                print(f"I can't do it, {COMPANION},"
                      "I can't do it, you say, your voice filled with emotion.")
                time.sleep(5)
                print(f"{COMPANION} looks at you with gratitude in their eyes,"
                      "and they fall to their knees, their eyes filled with tears.")
                time.sleep(5)
                print(f"Thank you, {USERNAME}, I knew you would come to save me,"
                      f"their voice filled with hope. :{COMPANION}")
                time.sleep(5)
                print("I can't kill you, even if you are corrupted, " \
                      "you say, your voice filled with emotion.")
                time.sleep(5)
                print("The book which you used to kill necronon, starts to pulse")
                time.sleep(5)
                print("All of a sudden, it opens and frees from your " \
                      "clutches and begins to float in the air.")
                time.sleep(5)
                print(f"{COMPANION} begins to float in the air alongside the book")
                time.sleep(5)
                print(f"Suddenly, lightning strikes {COMPANION}"
                      "and they collapse to the ground, weak but you feel " \
                      "that the dark energy is gone.")
                chapter_17()
            elif companion_choice3.lower() == "finish":
                print(f"You raise your sword and deliver the final blow to {COMPANION},"
                      "ending their corrupted existence.")
                time.sleep(5)
                print(f"With their last breath, {COMPANION} looks at you"
                      "with a mix of gratitude and sorrow.")
                time.sleep(5)
                print(f"Thank you for freeing me, {USERNAME}, {COMPANION}"
                      "whispers before fading away.")
                time.sleep(5)
                print("You look down at the remains of your once beloved Companion, your " \
                       "heart heavy with sorrow.")
                time.sleep(5)
                print("You begin to feel regret for what you have done.")
                time.sleep(5)
                print("You feel an awful sensation in your chest, "
                      "and you realize that you have lost a part of yourself.")
                time.sleep(5)
                print("You faint and collapse")
                time.sleep(5)
                print("You died, due to loneliness and sorrow")
                death()
                return
            else:
                print(f"Invalid choice. The corrupted {COMPANION} strikes you down,"
                      "and you fall to the ground, defeated.")
                time.sleep(5)
                death()
        else:
            print(f"Invalid choice. The corrupted {COMPANION} strikes you down,"
                  "and you fall to the ground, defeated.")
            time.sleep(5)
            death()
    else:
        print(f"Invalid choice. The corrupted {COMPANION} strikes you down,"
              "and you fall to the ground, defeated.")
        time.sleep(5)
        death()

def chapter_17():
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_17"
    print("***************************\n"
            "Chapter 17: The Princess?\n"
          "***************************\n")
    time.sleep(2)
    print(f"Uhhh, where am I?? {COMPANION} says, as they slowly regain consciousness. :{COMPANION}")
    time.sleep(5)
    print(f"What happened?, {COMPANION} asks, looking around the abandoned house.")
    time.sleep(5)
    print(f"You explain to {COMPANION} that you defeated necron and"
          "saved them from the dark energy that corrupted them.")
    time.sleep(5)
    print(f"{COMPANION} looks at you with gratitude in their eyes, and"
          "they fall to their knees, their eyes filled with tears.")
    time.sleep(5)
    print(f"Thank you, {USERNAME}, I knew you would come to save me,"
          f" their voice filled with hope. :{COMPANION}")
    time.sleep(5)
    print(f"You help {COMPANION} to their feet, and they look at you with gratitude in their eyes.")
    time.sleep(5)
    print(f"'Come let's go, we need to find the princess', you say to {COMPANION}")
    time.sleep(5)
    print(f"You and {COMPANION} leave the abandoned house and"
          "make your way to the heart of the capital.")
    time.sleep(5)
    print("As you walk through the empty streets, " \
          "you once again notice the strange symbols etched into the walls " \
          "but now they've seem to be faded away.")
    time.sleep(5)
    print(f"I want to get out of here, their voice filled with determination :{COMPANION}")
    time.sleep(5)
    print("You nod in agreement, determined to find the princess and escape the capital.")
    time.sleep(5)
    print("At the center of the capital, lies the princess's castle,"
          f" 'It's most likely she's trapped in there. :{COMPANION}")
    time.sleep(5)
    print(f"You and {COMPANION} make your way to the castle,"
          "hoping to find the princess and escape the capital.")
    chapter_18()

def chapter_18():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_18"
    print("***************************\n"
          "Chapter 18: The Castle\n"
          "***************************\n")
    time.sleep(2)
    print(f"You and {COMPANION} arrive at the castle,"
          "a grand gothic structure filled with towering walls and ornate decorations.")
    time.sleep(5)
    print("But something is off. The castle is eerily quiet, "
          "and you can feel a dark presence lurking in the shadows.")
    time.sleep(5)
    print(f"We need to find the princess and escape this place. :{COMPANION}")
    time.sleep(5)
    print("You nod in agreement, determined to find the princess and escape the capital.")
    time.sleep(5)
    print("As you explore the castle, " \
          "you come across a large underground chamber filled with darkness.")
    time.sleep(5)
    print("In the center of the chamber, you see a pedestal with a glowing purple key.")
    time.sleep(5)
    print("But before you can approach the pedestal, you hear a voice calling your name.")
    time.sleep(5)
    print("It's the princess, but something is off.")
    time.sleep(5)
    print("The princess appears before you, but her eyes are glowing with a dark energy.")
    time.sleep(5)
    print("The princess says, 'You have come far, but you will not find your way out of here.'")
    time.sleep(5)
    print("The voice is distorted and twisted, "
          "and you can feel a dark presence emanating from the princess.")
    time.sleep(5)
    print("****************************\n"
              "  Corrupted Princess \n"
          "****************************\n")
    time.sleep(5)
    print("You realize that the princess has been corrupted by " \
          "the dark energy of necron, and you must fight her to escape the capital.")
    time.sleep(5)
    princess_choice = input("Do you want to attack the princess "
                            "or try to reason with her? (Attack/Reason): ")
    if princess_choice.lower() == "reason":
        print("You try to reason with the princess, but she is too far gone.")
        time.sleep(5)
        death()
        return
    elif princess_choice.lower() == "attack":
        print("You draw your weapon and prepare to fight the corrupted princess.")
        time.sleep(5)
        print("The corrupted princess lunges at you, her claws slashing through the air.")
        time.sleep(5)
        print("You dodge the attack and strike back, hitting the princess in the side.")
        time.sleep(5)
        print("The corrupted princess lets out a roar of pain and anger.")
        time.sleep(5)
        print("You realize that you need to find another way to defeat her, "
              "and you quickly search the chamber for a way to " \
              "disable the dark energy that is corrupting her.")
        time.sleep(5)
        print(f"Before either you or {COMPANION} can react,"
               "the corrupted princess lunges at you again, her claws slashing through the air.")
        time.sleep(5)
        princess_choice2 = input("Do you want to attack the " \
                                 "princess again or try to run away? (Attack/Run): ")
        if princess_choice2.lower() == "attack":
            print(f"You and {COMPANION} attack the corrupted princess"
                  "with all your might, striking her with your weapons.")
            time.sleep(5)
            print("The corrupted princess roars in pain, but she is not defeated yet.")
            time.sleep(5)
            print("Suddenly, she summons a dark energy field that surrounds her, " \
                  "making her even more powerful and rendering your attacks useless.")
            time.sleep(5)
            print("You remember the book you found in the cavern, "
                  "and you quickly flip through the pages, " \
                  "searching for a spell that can help you defeat the corrupted princess.")
            time.sleep(5)
            print("You find a spell that seems to describe the princess, "
                  "and you quickly memorize it.")
            time.sleep(5)
            print("Nazma incus regina...")
            time.sleep(5)
            print("But before you can finish the spell, " \
                  "she lunges at you again, her claws slashing through the air.")
            time.sleep(5)
            death()
            return
        elif princess_choice2.lower() == "run":
            print(f"You and {COMPANION} try to run away from the corrupted princess,"
                  "dodging her attacks.")
            time.sleep(5)
            print(f"INCOMING ATTACK!!, :{COMPANION}")
            time.sleep(5)
            princess_choice3 = input("Type 'DUCK' to dodge the attack: ")
            if princess_choice3.lower() == "duck":
                print(f"You and {COMPANION} duck just in time,"
                      "avoiding the corrupted princess's attack.")
                time.sleep(5)
                print("You quickly search the chamber for a way to disable " \
                      "the dark energy that is corrupting her.")
                time.sleep(5)
                print("Before you can find a way to disable the dark energy, " \
                      "the book you found in the cavern starts to pulse.")
                time.sleep(5)
                print("It levitates into the air and opens, " \
                      "revealing a passage that seems to describe the princess.")
                time.sleep(5)
                print("Suddenly, lightning strikes the book, "
                      "and it begins to glow with a bright light.")
                time.sleep(5)
                print("The book strikes you with lightning, "
                      "and you can feel its power coursing through your veins.")
                time.sleep(5)
                print("You realize that you can use this power to help the corrupted princess.")
                time.sleep(5)
                print("You quickly memorize the passage and prepare to cast the spell.")
                time.sleep(5)
                print("Nazma incus regina! you chant, and a burst of light erupts from your hands.")
                time.sleep(5)
                print("The corrupted princess roars in pain, and you " \
                      "can see the dark energy surrounding her begin to dissipate.")
                time.sleep(5)
                print("AHHHHHHHHHHHHHHHHHHHHHH, NOOOOOOOOOOOOOOOO! The " \
                      "corrupted princess screams as she begins to weaken.")
                time.sleep(5)
                print("THIS WILL NOT BE THE END, YOU WILL NEVER ESCAPE THIS PLACE ALIVE! " \
                      " the princess screams as she falls to the ground, defeated.")
                time.sleep(5)
            else:
                print("You fail to dodge the attack, the " \
                      "corrupted princess strikes you down, and you fall to the ground, defeated.")
                time.sleep(5)
                death()
                return
        else:
            print("Invalid choice. The corrupted princess strikes you down, "
                 "and you fall to the ground, defeated.")
            time.sleep(5)
            death()
    else:
        print("Invalid choice. The corrupted princess strikes you down, "
              "and you fall to the ground, defeated.")
        time.sleep(5)
        death()

def chapter_19():
    global  CURRENT_CHAPTER
    CURRENT_CHAPTER = "chapter_19"
    print("***************************\n"
          "Chapter 19: The Aftermath\n"
          "***************************\n")
    time.sleep(2)
    print(f"You and {COMPANION} stand over the defeated corrupted princess,"
          "her body lying motionless on the ground.")
    time.sleep(5)
    print("You realize that you have defeated the final beast,"
           "but at a great cost.")
    time.sleep(5)
    print("You look down at the remains of the corrupted princess, your heart heavy with sorrow.")
    time.sleep(5)
    print("You begin to feel regret for what you have done.")
    time.sleep(5)
    print("Suddenly, you hear the princess slowly waking up")
    time.sleep(5)
    print("Uhhh, where am I??  as she slowly regains consciousness. :Princess Violet")
    time.sleep(5)
    print("What happened?, looking around the chamber. :Princess Violet")
    time.sleep(5)
    print("You explain to the princess that you defeated the corrupted " \
          "princess and saved her from the dark energy that corrupted her.")
    time.sleep(5)
    print("The princess looks at you with gratitude in her eyes.")
    time.sleep(5)
    print(f"Thank you, {USERNAME}, I knew you would come to save me. :Princess Violet")
    time.sleep(5)
    print("You help the princess to her feet, and she looks at you with a newfound determination.")
    time.sleep(5)
    print(f"Now, me and {COMPANION} really need to get out of here, you say to the princess.")
    time.sleep(5)
    print(f"Yeah, I would like to get out of here too, :{COMPANION}"
          "their voice still filled with pain.")
    time.sleep(5)
    print(f"You and {COMPANION} leave the chamber with the princess towards"
          "one of the castle's dungeon rooms")
    the_end()
#Goes to the end

def the_end():
    global CURRENT_CHAPTER
    CURRENT_CHAPTER = "the_end"
    print("***************************\n"
                   "The End\n"
          "***************************\n")
    time.sleep(2)
    print(f"You,{COMPANION} and the princess reach the portal that"
          "leads out of Fargon towards where you came from")
    time.sleep(5)
    print("The magnificent green portal is glowing with a bright light,"
          "and you can feel its power coursing through your veins.")
    time.sleep(5)
    print(f"Well, this is it, you and {COMPANION}"
          "say to the princess.")
    time.sleep(5)
    print("This is goodbye")
    time.sleep(5)
    print(f"Suddenly, the princess pulls you and {COMPANION} into a tight embrace.")
    time.sleep(5)
    print(f"Thank you, {USERNAME} and {COMPANION},"
          "for saving me and for everything you have done. :Princess Violet")
    time.sleep(5)
    print("Fargon will never forget your bravery and heroism. :Princess Violet")
    time.sleep(5)
    print(f"You and {COMPANION} nod in agreement, grateful for the princess's kind words.")
    time.sleep(5)
    print("Suddenly you feel a strange sensation in your chest, "
          "and you realize that you've survived so many days in Fargon")
    time.sleep(5)
    final_choice = input("Do you want to stay in Fargon or return home? (Stay/Return): ")
    if final_choice.lower() == "stay":
        print(f"You and {COMPANION} decide to stay in Fargon,"
              "determined to continue your adventures and protect the realm.")
        time.sleep(5)
        print(f"You and {COMPANION} are now the heroes of Fargon,"
              "and your legend will live on for generations to come.")
        time.sleep(5)
        credits()
    #Goes to credits by choosing to stay
    elif final_choice.lower() == "return":
        credits()
    #Returns home and goes to credits
    else:
        print(f"Invalid choice, You and {COMPANION} decide to return home,"
              "grateful for the adventures you have had in Fargon.")
        time.sleep(5)
        print("You say goodbye to the princess,"
              "promising to never forget your time in Fargon.")
        time.sleep(5)
        print(f"You and {COMPANION} step through the portal, ready to return to your world.")
        time.sleep(5)
        print(f"You and {COMPANION} are now the heroes of Fargon,"
              "and your legend will live on for generations to come.")
        time.sleep(5)
        save_game()
        credits()
    #Goes to credits

def credits():
    print("***************************\n"
          "         Credits\n"
          "***************************\n")
    time.sleep(2)
    print(CREDIT_ROLL)
    time.sleep(2)
    print("Game made by: Eric")
    time.sleep(2)
    print("Special Thanks to..")
    time.sleep(1)
    print("Goodbye!")
    time.sleep(2)
    secret = input("Would you like to see a secret ending? (Yes/No): ")
    if secret.lower() == "yes":
        print("***************************\n"
              "secret Ending: The Dark Path\n"
              "***************************\n")
        #Seperate ending
        time.sleep(2)
        print(f"You and your COMPANION, {COMPANION}, decide to take a different path.")
        time.sleep(5)
        print("Instead of returning home, you choose to explore the dark side of Fargon.")
        time.sleep(5)
        print("You become the rulers of Fargon, feared and respected by all.")
        time.sleep(5)
        print("Your legend lives on, but it is a dark one.")
        time.sleep(5)
        print("You are known as the Dark Lords of Fargon, and your reign lasts for centuries.")
        time.sleep(5)
        print("You eventaully get defeated by a group of heroes who rise up against you.")
        time.sleep(5)
        print("For when there is darkness, there is light...")
        time.sleep(5)
        print("Thank you again. For playing this game")
        the_end()
    else:
        print("Thank you again. For playing this game")
        the_end()


def story_over():
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
#Prints each character one by one, takes a while
#End of game

if __name__ == "__main__":
    main()
#Used due to multiple functions
