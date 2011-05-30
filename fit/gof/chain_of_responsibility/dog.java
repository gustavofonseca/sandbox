class Dog extends Animal {
	public void processRequest(String request) {
	    Boolean isDog = request.contains("auau") ? true : false;
	    
	    if(isDog){
	        System.out.println("handled by a Dog instance!");
 	    } else if (successor != null){
	        successor.processRequest(request);
	    } else {
	        System.out.println("Dog does not have a successor =/");
	    }
	}
}