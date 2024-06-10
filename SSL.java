

import java.util.Iterator;

public class SSL<E> implements Iterable<E> {
	
	private SNode<E> head;
	private SNode<E> tail;
	private int length = 0;
	
	private class SNode <E> {
		 E value;
		 SNode<E> next;
		
		public SNode(E value, SNode<E> next) {
			this.value = value;
			this.next = next;
		}
		
		public SNode(E value) {
			this.value = value;
		}
		
		public String toString() {
			return "("+this.value.toString()+") -> ";
		}
	}
	
	private class SSLIterator <E> implements Iterator<E> {
		 SNode<E> curr;
		 
		public SSLIterator(SNode<E> head) {
			this.curr = head;
		}
		@Override
		public boolean hasNext() {
			return curr!=null;
		}
		
		public SNode<E> nextNode() {
			SNode<E> node = curr;
			curr = curr.next;
			return node;
		}

		@Override
		public E next() {
			E value = curr.value;
			curr = curr.next;
			return value;
			
		}}
	
	
	
	
	public void removeTail() {
		if (this.isEmpty()) {
			return;
			
		}else if (this.head.next==null) {
			this.clear();
		}
		
		else {
			SSLIterator<E> iterator = this.iterator();
			while (iterator.curr.next!=this.tail){	
				iterator.nextNode();
			}
			this.tail = iterator.curr;
			this.tail.next = null;
			this.length-=1;
			
		}
		
	}
	
	public void clear() {
		this.head = this.tail = null;
		this.length = 0;
	}
	
	public void removeHead() {
		if (this.isEmpty()) {
			return;
		}else if (this.head.next==null) {
			this.clear();
		} 
		else {
			this.head = this.head.next;
			this.length-=1;
		}
	}
	
	public void addTail(E value) {
		if (this.isEmpty()) {
			this.tail = this.head = new SNode<E>(value);
		}else {
			this.tail.next = new SNode<E>(value);
			this.tail = this.tail.next;
		}
		this.length+=1;
	}
	
	public void addHead(E value) {
		if (this.isEmpty()) {
			this.tail = this.head = new SNode<E>(value);
			
		}else {
			SNode<E> newHead = new SNode<E>(value, this.head);
			this.head = newHead;
			
		}
		this.length+=1;
		
	}
	
	public boolean isEmpty() {
		return this.head==null;
	}
	
	
	
	public String toString() {
		String rep = "";
		SSLIterator<E> iterator = this.iterator();
		while (iterator.hasNext()){	
			rep+=iterator.nextNode().toString();
		}
		return rep;
	}

	@Override
	public SSLIterator<E> iterator() {
		return new SSLIterator<E>(this.head);
	}
	public int getLength() {
		return this.length;
	}
	

}
