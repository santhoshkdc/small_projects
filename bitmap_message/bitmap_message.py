import sys

bitmap ="""
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** **************  *
           *********            *******   **************** *  *
            ********           ***************************   **
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **    **  *
                 ********        *************    *   ** ***
                   ********         ********           * *** ****
                   *********         ******           **** ** * **
                   *********         ******   *            *** *   *
                     ******          *****  *               ***   *
                     *****            ****  *            *** ****
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print("What message do you ant to type on your map?")
message = ""
while len(message) == 0:
    message = input("\n> ")
if message.lower() == 'q':
    sys.exit()


for lines in bitmap.splitlines():
    for i, bits in enumerate(lines):
        if bits == " ":
            print(" ", end="")
        else:
            print(message[i % len(message)], end="")
    print()
