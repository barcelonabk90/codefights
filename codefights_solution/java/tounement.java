
class Tounement {

    /**
     * Given a number of the pages in some book find the number of digits one
     * needs to print to enumerate the pages of the book.
     *
     * Example
     *
     * For n = 11, the output should be pagesNumbering(n) = 13.
     *
     * @param n
     * @return
     */
    int pagesNumbering(int n) {
        int c = 0;
        int a = n;
        while (a > 0) {
            a = (int) a / 10;
            c += 1;
        }
        if (c == 1) {
            return n;
        }
        int cnt = 1;
        int res = 9;
        int cur = 9;
        while (cnt < c) {
            cnt += 1;
            res += (int) (Math.pow(10, cnt) - cur - 1) * cnt;
            cur = (int) Math.pow(10, cnt) - 1;
        }
        return res + (n - cur) * cnt;
    }

    /**
     *
     * @param l
     * @param r
     * @return
     */
    int specialNumbers(int l, int r) {
        int res = 0;
        for (int i = l; i <= r; i++) {
            if (special(i)) {
                res++;
            }
        }
        return res;
    }

    boolean special(int a) {
        int n = a;
        List<Integer> arr = new ArrayList<Integer>();
        while (a > 0) {
            int tmp = a % 10;
            if (tmp != 0 && tmp != 6 && tmp != 8 && tmp != 9) {
                return false;
            }
            arr.add(tmp);
            a = (int) Math.floor(a / 10);
        }
        List<Integer> arr1 = new ArrayList<Integer>();
        int cnt = arr.size();
        for (int i = 0; i < cnt; i++) {
            int c = arr.get(i);
            if (c == 0 || c == 8) {
                arr1.add(c);
            } else {
                arr1.add(15 - c);
            }
        }

        for (int i = 0; i < cnt; i++) {
            if (arr.get(i) != arr1.get(cnt - i - 1)) {
                return false;
            }
        }
        return true;

    }

    /**
     * Write an algorithm that constructs an array of non unique prime factors
     * of a number n.
     *
     * Example
     *
     * For n = 100, the output should be primeFactors(n) = [2, 2, 5, 5].
     *
     * @param n
     * @return
     */
    int[] primeFactors(int n) {
        List<Integer> res = new ArrayList<Integer>();
        int i = 2;
        while (n > 1) {
            while (n % i == 0) {
                res.add(i);
                n = (int) Math.floor(n / i);
            }
            i++;
        }
        return res.stream().mapToInt(Integer::intValue).toArray();
    }

    String[] isDivisibleBy3(String a) {
        List<String> res = new ArrayList<String>();
        for (int i = 0; i < 10; i++) {
            String c = "" + i;
            String tmp = a.replace("*", c);
            if (divisible3(tmp)) {
                res.add(tmp);
            }
        }
        String[] stockArr = new String[res.size()];
        return res.toArray(stockArr);

    }

    boolean divisible3(String a) {
        int sum = 0;
        for (char c : a.toCharArray()) {
            int digit = c - '0';
            sum += digit;
        }
        return sum % 3 == 0;

    }

}
