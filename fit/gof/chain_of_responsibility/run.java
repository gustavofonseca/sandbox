class Run {
	public static void main(String[] args) {
		Dispatcher dispatcher = new Dispatcher();
		dispatcher.handleForMe("the animal who says \"auau\"");
		dispatcher.handleForMe("the animal who says \"miau\"");
		dispatcher.handleForMe("the animal who says \"hakuna matata\"");
	}
}