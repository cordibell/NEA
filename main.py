# main file, made 5/9/24

import login_gui
import login_code
import join_events
import join_events_code


login_window = login_gui.login_menu()

join_events_window = join_events.join_events_menu(login_window)

login_window.mainloop()