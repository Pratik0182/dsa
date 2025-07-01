int possibleStringCount(char* word) {
    int i = 0, curr = word[0], cnt = 0, res = 0;
    while (word[i] != '\0'){
        if (curr == word[i]) cnt++;
        else{
            res += cnt - 1;
            curr = word[i];
            cnt = 1;
        }
        i++;
    }
    res += cnt;
    return res;
}