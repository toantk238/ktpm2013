import static org.junit.Assert.*;

import org.junit.Test;


public class Giai_PTB1Test {

	@SuppressWarnings("deprecation")
	@Test
	public void testPTB1() {
		Giai_PTB1 tester = new Giai_PTB1();
		
		assertEquals(  -1 , tester.PTB1(1, 1), 0 );	
		assertEquals(  10 , tester.PTB1(9, -90), 0 );	
		//assertEquals(  10.5  , tester.PTB1(0, 5), 0 );	
		//assertEquals(  0 , tester.PTB1(5, 0), 0 );	
	}

}
