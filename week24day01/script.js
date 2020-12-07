var count = 0;

while (true){
    const num = Math.ceil(Math.random() * 20);
    console.log(num);
    count += 1;
    const gnum = prompt('Guess the number between 1 and 20 inclusive');
    if (gnum == num ){
        if (count === 2){
            console.log('Matched: win');
            break;
        }
        else{
            continue;
        }

    }else{
        console.log('Loose')
        break;
    }
}

     
  
