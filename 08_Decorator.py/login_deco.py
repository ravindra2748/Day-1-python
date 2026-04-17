is_logged_in = False

def login_required(func):
    def wrapper(*args,**kwargs):
        if not is_logged_in:
            print("❌ Access denied! Please log in first.")
            return
        return func(*args,**kwargs)
    return wrapper






def login(username,password):
    global is_logged_in
    if username == "admin" and password == "1234":
        is_logged_in = True
        print("✅ Login successful!")
    else:
         print("❌ Invalid credentials!")

@login_required
def view_dashboard():
    print("📊 Welcome to your dashboard!")

view_dashboard()
login("admin","1234")
view_dashboard()