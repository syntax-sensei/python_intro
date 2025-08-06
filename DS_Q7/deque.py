from collections import deque

class BrowserHistory:
    def __init__(self, max_size=5):
        """
        Initialize browser history with maximum size.
        
        Args:
            max_size (int): Maximum number of pages to keep in history
        """
        self.max_size = max_size
        self.history = deque(maxlen=max_size)  # Main history with auto-removal of oldest
        self.forward_stack = deque()  # Stack for forward navigation
    
    def add_page(self, url):
        """
        Add a new page to the browser history.
        
        Args:
            url (str): URL of the new page to visit
        """
        # Clear forward stack when visiting a new page
        self.forward_stack.clear()
        
        # Add new page to history (oldest will be auto-removed if max_size exceeded)
        self.history.append(url)
        
        print(f"Visited: {url}")
        self.show_state()
    
    def go_back(self):
        """
        Go back to the previous page.
        Moves the current page to forward stack and removes it from history.
        """
        if len(self.history) <= 1:
            print("Cannot go back - no previous pages available")
            return
        
        # Move current page (last in history) to forward stack
        current_page = self.history.pop()
        self.forward_stack.append(current_page)
        
        print(f"Went back from: {current_page}")
        if self.history:
            print(f"Current page: {self.history[-1]}")
        self.show_state()
    
    def go_forward(self):
        """
        Go forward to a previously backed-out page.
        Moves the most recent page from forward stack back to history.
        """
        if not self.forward_stack:
            print("Cannot go forward - no forward pages available")
            return
        
        # Move most recent page from forward stack back to history
        forward_page = self.forward_stack.pop()
        self.history.append(forward_page)
        
        print(f"Went forward to: {forward_page}")
        self.show_state()
    
    def get_current_page(self):
        """
        Get the current page (most recent in history).
        
        Returns:
            str: Current page URL or None if no pages in history
        """
        return self.history[-1] if self.history else None
    
    def show_state(self):
        """
        Display the current state of history and forward stack.
        """
        print(f"History: {list(self.history)}")
        print(f"Forward Stack: {list(self.forward_stack)}")
        print(f"Current Page: {self.get_current_page()}")
        print("-" * 50)

def main():
    """
    Demonstrate the browser history system with various operations.
    """
    print("=== Browser History System Demo ===\n")
    
    # Create browser history instance
    browser = BrowserHistory(max_size=5)
    
    # Test adding pages
    print("1. Adding pages to history:")
    browser.add_page("https://google.com")
    browser.add_page("https://github.com")
    browser.add_page("https://stackoverflow.com")
    browser.add_page("https://python.org")
    browser.add_page("https://docs.python.org")
    
    # Test adding one more page (should remove oldest)
    print("2. Adding 6th page (should remove oldest):")
    browser.add_page("https://realpython.com")
    
    # Test going back
    print("3. Going back twice:")
    browser.go_back()
    browser.go_back()
    
    # Test going forward
    print("4. Going forward once:")
    browser.go_forward()
    
    # Test adding new page after going back (should clear forward stack)
    print("5. Adding new page after going back:")
    browser.add_page("https://leetcode.com")
    
    # Test edge cases
    print("6. Testing edge cases:")
    browser.go_forward()  # Should show error message
    
    # Go back to first page
    while len(browser.history) > 1:
        browser.go_back()
    
    browser.go_back()  # Should show error message
    
    print("\n=== Demo Complete ===")

if __name__ == "__main__":
    main()