n=gets.to_i
$><<%w{ace two three four five six seven eight nine ten jack queen king}[n%13]+' of '+%w{heart spade diamond club}[n/-13*-3/4%4]+?s
