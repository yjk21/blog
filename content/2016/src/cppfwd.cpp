#include <iostream>
#include <armadillo>
#include <chrono>

using namespace std;
using namespace chrono;

/*
 * Inputs:
 * - px:  pointer to sequence array
 * - S:   length of sequence
 * - ph:  pointer to initial hidden state (will be overwritten)
 * - pWh: pointer to transition matrix
 * - pWi: pointer to input embedding
 * - D:   number of hidden neurons
 * - M:   number of items
 */
extern "C" double fwd(int64_t * px, int S, double * ph, double * pWh,double * pWi,  int D , int M);

double fwd(int64_t * px, int S, double * ph, double * pWh,double * pWi,  int D , int M){
    //wrap raw input pointers in Armadillo objects
    arma::Col<int64_t> x(px, S, false, false);
    arma::mat Wh(pWh, D, D, false, false);
    arma::mat Wi(pWi, D, M, false, false);
    arma::vec h(ph, D, false, false);

    //allocate vector of activations at time t
    arma::vec at(D);

    //tic...
    high_resolution_clock::time_point tic = high_resolution_clock::now();
    for(auto xt : x){
        at = Wh * h + Wi.col(xt);
        h = 1.0 / (1.0 + exp(-at));
    }
    //...toc
    high_resolution_clock::time_point toc = high_resolution_clock::now();

    auto duration = duration_cast<microseconds>( toc - tic  ).count();
    chrono::duration<double> fp_ms = toc - tic;
    return fp_ms.count();
}

