nt lastCoin = 0;

for (int coin: coins) {

    // Recursively we explore each currency option
    // In each recursive call we pass the remaining amount as an argument in the case of using that currency.
    int newMin = recursion (currencies, remainder - currency, dp, lastUsedCoins);

    // If the current result is less than the one we already had, we replace that as the new minimum so far
    if (newMin> = 0 && newMin <currMin) {
        // We save the currency used in this new minimum
        lastCoin = currency;
        // We save the result obtained as the minimum so far
        currMin = 1 + newMin;
        }
    
    // If the result is different from our initial large value (that is, a solution was not found) we put the arbitrary value of -1
    // Otherwise, we save the value that we have found
    dp [remainder] = (currMin == 1000000)? -1: currMin;

    // If a solution was found, we save the currency that was finished using, to later rebuild
    lastUsedCoins [remainder] = (currMin == 1000000)? -1: lastCoin;

    // We copy the vector of the coins used to reconstruct it later
    globalCoinsUsed = lastUsedCoins;

    // We return the minimum result
    return dp [remainder];
    };


int main () {
    // First receive the quantity to be solved
    int amount;
    cin >> amount;

    // Then the denominations of currencies that will be used
    vector <int> coins;
    rope temperature;

    // We delete the cin stream to be able to read the denominations in a single line
    cin.ignore ();
    getline (standard :: cin, temp);

    // All this code works to parse a string to whole numbers and store them in a vector.
    chain current (temp);

    while (1) {
        int n;
        current >> n;
        coins.push_back (n);
        if (! stream) {
        pause;
        }
        }


    // We instantiate the class of the solution
    Inst solution;
    int result = inst.leastCoins (coins, amount);

    // We print the result
    cout << endl << result << endl;

    // To rebuild and print the coins used in the optimal solution
    inst.printCoinsUsed (globalCoinsUsed, amount);
    while (! sortedCoins.empty ()) {
        cout << sorted coins.top () << "";
        sortedCoins.pop ();
        }
    return 0;
    }