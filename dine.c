/*Lab 4 dining philosphers problem*/
#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
pthread_mutex_t mutex[5];

void* pickup_forks(int num){
int left,right;
    if(num < 4){
        right = num;
        left = right + 1;
    }
    else if(num == 4){
        //special case for philospher 4
        right = 0;
        left = num;
    }
    //lock right
        pthread_mutex_lock(&mutex[right]);
        //try to lock left
        if(pthread_mutex_trylock(&mutex[left]) == 0){
            //eat
            printf("The philospher %d is eating\n", num);
            
        }

}

void* return_forks(int num){
int left,right;
    if(num < 4){
        right = num;
        left = right + 1;
    }
    else if(num == 4){
        //special case for philospher 4
        right = 0;
        left = num;
    }
    //unlock left
    pthread_mutex_unlock(&mutex[left]);
    //unlock right
        pthread_mutex_unlock(&mutex[right]);
        float time = ((float)rand()/(float)(RAND_MAX)) * 2.0 + 1;//random float from 1.0 to 3.0
        printf("The philospher %d is thinking for %f seconds\n", num,time);
        sleep(time);
    
    
	
}

void* philospher(void* arg)
{
    int num = (int)arg;
   
    while(1){
        pickup_forks(num);
        return_forks(num);
    }
}
int main()
{
    pthread_t p[5];
    //init
    for(int i = 0;i < 5;i++) pthread_mutex_init(&mutex[5],NULL);
    //create
    for(int i = 0;i < 5;i++) pthread_create(&p[i],NULL,philospher,(void*)i);
    //join
    for(int i = 0;i < 5;i++) pthread_join(p[i],NULL);
    //destroy
    for(int i = 0;i < 5;i++) pthread_mutex_destroy(&mutex[i]);
    return 0;
}
