#Example setup for this particular repository
#should be run before anything else, e.g. include into .juliarc.jl

#setup search path for julia modules
push!(LOAD_PATH, pwd())
push!(LOAD_PATH, joinpath(homedir(), "repos","utils","julia"))
push!(LOAD_PATH, joinpath(homedir(), "repos","blog","content", "2016", "src"))

#setup search path for python modules
import PyCall
pp = [p::AbstractString  for p in PyCall.pyimport("sys")["path"]]

pypath = joinpath(homedir(), "repos","blog","content", "2016", "src")

if !any(map(x->x == pypath, pp))
    unshift!(PyCall.PyVector(PyCall.pyimport("sys")["path"]), pypath)
end

