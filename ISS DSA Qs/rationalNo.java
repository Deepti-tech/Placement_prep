public class rationalNo{
    private int numerator;
    private int denominator;

    private rationalNo (int numerator, int denominator){
        try{
            this.numerator = numerator;
            this.denominator = denominator;        
        }catch(Exception e){
            System.out.println(e);
        }
    }
    public rationalNo add(rationalNo secNo){
        int newNum = this.numerator*secNo.denominator + secNo.numerator*this.denominator;
        int newDen = this.denominator + secNo.denominator;

        return new rationalNo(newNum, newDen);
    }
    @Override
    public String toString() {
        return numerator + "/" + denominator;
    }
    public static void main(String[] args) {
    rationalNo r1 = new rationalNo(1,5);
    rationalNo r2 = new rationalNo(2, 3);
    rationalNo sum = r1.add(r2);
    System.out.println(sum);
    }
}

// The first question was to create a class of rational numbers. 
// The class accepts 2 inputs: numerator and denominator.
// I had to add 2 rational objects and output a new rational object. 