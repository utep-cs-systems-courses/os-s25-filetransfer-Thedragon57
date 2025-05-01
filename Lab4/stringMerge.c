#include <stdio.h>
#include <string.h>


// char * mergeAlternately(char * word1, char * word2){
//     int i = 0;
//     char final[20];
//     while(*word1 != '\0' || *word2 != '\0' || i != 3){
//         final[i] = *word1;
//         i++;
//         final[i] = *word2;
//         //final[i+1] = word2[j];
//         word1++;
//         word2++;
//     }
//     return final;
// }


int main(int argc, char const *argv[])
{
    char *test1 = "abc";
    char *test2 = "pqr";

    printf("%c\n", *test1);
    //mergeAlternately(test1,test2);
    return 0;
}