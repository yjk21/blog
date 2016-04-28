module mymod
sigmoid(v) = 1.0 ./ (1.0 + exp(-v))

function step(xt, htm1, Wh, Wi)
    return sigmoid(Wh * htm1 + Wi[:,xt])
end

function jlfwd(x,h0, Wh, Wi)
    ht = h0
    tic()
    for xt in x
        ht = step(xt, ht, Wh, Wi)
    end
    toc = toq()
    return ht, toc
end

function cppfwd!(x::Array{Int,1}, h0::Array{Float64,1}, Wh::Array{Float64,2}, Wi::Array{Float64,2})
    S = length(x)
    D,M=size(Wi)
    D1,D2 = size(Wh)
    D3 = length(h0)
    assert(D1 == D2)
    assert(D == D1)
    assert(D == D3)
    assert(minimum(x)>=0)
    assert(maximum(x)<M)
    return ccall( (:fwd,"libmytest0"), Cdouble, (Ptr{Int}, Int32, Ptr{Cdouble}, Ptr{Cdouble},Ptr{Cdouble}, Int32, Int32),x, S, h0, Wh, Wi, D, M )
end



end
