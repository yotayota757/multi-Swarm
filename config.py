class Config:
    __PopulationSize = 30 # Population Size (default = 15)
    __MaxDomain = 500 # variable upper limit
    __MinDomain = -500 # variable lower limit
    __Lambda = 1.5 # parameter for Levy flight
    __Pa = 0.25
    __StepSize = 0.01
    __Dimension = 2 # The number of dimension
    __F = 0.8 # differential weight
    __CR = 0.5 # crossover probability
    __W = 0.9 # inertia weight
    __C1 = 1.5 # weight for personal best
    __C2 =  1.5# weight for global best
    __Trial = 31
    __Iteration = 9000
    __Function = "NaN"
    __N = 10
    __Beta = 0.01
    __Radius = 350
    __Rnd = 0



    """For ALL"""
    # Population Size
    @classmethod
    def get_population_size(cls):
        return cls.__PopulationSize

    @classmethod
    def set_population_size(cls,population):
        cls.__PopulationSize = population

    # Domain
    @classmethod
    def get_max_domain(cls):
        return cls.__MaxDomain

    @classmethod
    def set_max_domain(cls, _max_domain):
        cls.__MaxDomain = _max_domain

    @classmethod
    def get_min_domain(cls):
        return cls.__MinDomain

    @classmethod
    def set_min_domain(cls, _min_domain):
        cls.__MinDomain = _min_domain

    # Dimension
    @classmethod
    def get_dimension(cls):
        return cls.__Dimension

    @classmethod
    def set_dimension(cls, dimension):
        cls.__Dimension = dimension

    @classmethod
    def get_function(cls):
        return cls.__Function

    @classmethod
    def set_function(cls, function):
        cls.__Function = function

    # Iteration
    @classmethod
    def get_iteration(cls):
        return cls.__Iteration

    @classmethod
    def set_iteration(cls,iteration):
        cls.__Iteration = iteration

    # Trial
    @classmethod
    def get_trial(cls):
        return cls.__Trial

    """For Cuckoo Search"""
    # lambda
    @classmethod
    def get_lambda(cls):
        return cls.__Lambda

    @classmethod
    def set_lambda(cls, _lambda):
        cls.__Lambda = _lambda

    # Pa
    @classmethod
    def get_Pa(cls):
        return cls.__Pa

    @classmethod
    def set_Pa(cls, Pa):
        cls.__Pa = Pa

    # StepSize
    @classmethod
    def get_step_size(cls):
        return cls.__StepSize

    @classmethod
    def set_step_size(cls, stepsize):
        cls.__StepSize = stepsize

    """For Differential Evolution"""
    # F (Scale Parameter)
    @classmethod
    def get_F(cls):
        return cls.__F

    @classmethod
    def set_F(cls, F):
        cls.__F = F

    # CR (Crossover Rate)
    @classmethod
    def get_CR(cls):
        return cls.__CR

    @classmethod
    def set_CR(cls, CR):
        cls.__CR = CR

    """For Particle Swarm Optimization"""
    # W (weight)
    @classmethod
    def get_W(cls):
        return cls.__W

    @classmethod
    def set_W(cls, W):
        cls.__W = W

    # C1
    @classmethod
    def get_C1(cls):
        return cls.__C1

    @classmethod
    def set_C1(cls,C1):
        cls.__C1 = C1

    # C2
    @classmethod
    def get_C2(cls):
        return cls.__C2

    @classmethod
    def set_C2(cls, C2):
        cls.__C2 = C2


    @classmethod
    def get_N(cls):
        return cls.__N

    @classmethod
    def set_N(cls,n):
        cls.__N = n

    @classmethod
    def get_Beta(cls):
        return cls.__Beta

    @classmethod
    def set_Beta(cls,beta):
        cls.__Beta = beta

    @classmethod
    def get_Radius(cls):
        return cls.__Radius

    @classmethod
    def set_Radisu(cls,radius):
        cls.__Radius = radius

    @classmethod
    def get_Rnd(cls):
        return cls.__Rnd

    @classmethod
    def set_Rnd(cls, rnd):
        cls.__Rnd = rnd





