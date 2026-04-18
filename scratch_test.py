from ui import JarvisUI
import time
import threading

def run_test():
    ui = JarvisUI("face.png")
    
    def simulate_wake():
        print("Simulate wake up...")
        ui.set_state("LISTENING")
        print("Wake up scheduled.")
        
    def close_sim():
        print("Closing window (simulate X click from MAIN thread)...")
        ui._on_window_close()
        
        # Schedule wake after 2 sec
        ui.root.after(2000, simulate_wake)
        
        # Schedule exit after 5 sec
        ui.root.after(5000, ui.root.destroy)
        print("Close logic done.")

    # Schedule the X click from main thread after 2 sec
    ui.root.after(2000, close_sim)
    
    ui.root.mainloop()
    print("Done.")

if __name__ == "__main__":
    run_test()
