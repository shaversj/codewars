import java.util.Arrays;

public class SpinWords {
    // https://www.codewars.com/kata/5264d2b162488dc400000001/train/java

    public String spinWords(String sentence) {
        String[] split_sentence = sentence.split(" ");
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < split_sentence.length; i++){
            if(split_sentence[i].length() >= 5) {
                if(i > 0){
                    sb.append(" ").append(reverseWord(split_sentence[i]));
                } else {
                    sb.append(reverseWord(split_sentence[i]));
                }
            } else if (i > 0){
                sb.append(" ").append(split_sentence[i]);
            } else {
                sb.append(split_sentence[i]);
            }
        }
        return sb.toString();
    }

    private String reverseWord(String word){
        StringBuilder reversedWord = new StringBuilder();
        char[] wordToArray = word.toCharArray();

        for(int i = wordToArray.length - 1; i >= 0; i--){
            reversedWord.append(wordToArray[i]);
        }
        return reversedWord.toString().trim();
    }

    public static void main(String[] args) {
        SpinWords s = new SpinWords();
        System.out.println(s.spinWords("Hey fellow warriors"));
        System.out.println(s.spinWords("Hey fellow warriors").equals("Hey wollef sroirraw"));
    }
}
