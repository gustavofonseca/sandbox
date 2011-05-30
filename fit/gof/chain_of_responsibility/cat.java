class Cat extends Animal {
	public void processRequest(String request) {
	    Boolean isCat = request.contains("miau") ? true : false;
	    
	    if(isCat){
	        System.out.println("handled by a Cat instance!");
 	    } else if (successor != null){
	        successor.processRequest(request);
	    } else {
	        System.out.println("Cat does not have a successor =/");
	    }
	}
}