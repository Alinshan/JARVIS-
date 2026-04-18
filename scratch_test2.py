import sys
import time
import threading
import asyncio
import os

def run():
    if "--hidden" not in sys.argv:
        sys.argv.append("--hidden")  # Start hidden!
    from main import main, JarvisLive
    
    original_run = JarvisLive.run
    
    async def hooked_run(self):
        async def background_waker():
            print("Background waker starting...")
            await asyncio.sleep(3)
            print("Simulating a clap!")
            self.wake_reason = "clap"
            self.wake_detected.set()
            print("Clap fired.")
            
            await asyncio.sleep(8)
            print("Exiting...")
            self.ui.root.after(0, self.ui.root.destroy)
        
        asyncio.create_task(background_waker())
        try:
            await original_run(self)
        except Exception as e:
            print("Crash in original run:", e)
        
    JarvisLive.run = hooked_run
    
    print("Starting main...")
    try:
        main()
    except Exception as e:
        print("Crash in main:", e)

if __name__ == "__main__":
    run()
