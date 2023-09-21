# Epic Seven auto Shop Refresh
 E7 auto shop refresh inspired from @ema to fix edge cases.
 Check out the original code and how to set it up at https://github.com/EmaOlay/E7-Auto-Shop-Refresh 

# Issues
- 1. If Covenant bookmark and Mystic medal appear at the same time. It will only purchase the covenant bookmark and ignore the Mystic medal
- 2. If Covenant bookmark or Mystic medal appear at the last row of the shop after scrolling, it will be ignored.

# Fixes
- 1. Fixed by adding a delay after each purchase to ensure both gets checked
- 2. Fixed by checking again for both Covenant bookmark and Mystic medal after scrolling

# QOL
Added global variable to make it easier to customize the waiting time/scrolling pixel 

