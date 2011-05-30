class Dispatcher {
    Cat cat = new Cat();
    Dog dog = new Dog();
        
    public void handleForMe(String request) {
        cat.successor = dog;
        cat.processRequest(request);
    }    
}