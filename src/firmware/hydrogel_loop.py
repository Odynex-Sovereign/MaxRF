import time

class HydrogelThermalLoop:
    def __init__(self):
        self.lower_critical_solution_temp = 42.0 # Temperature point where hydrogel contracts to "sweat"
        self.is_recharging = False

    def evaluation_cycle(self, core_temp_c: float, ambient_humidity_pct: float) -> str:
        """
        Continuously evaluates whether the composite structural casing should 
        sweat moisture away or harvest water content directly from room air humidity.
        """
        if core_temp_c >= self.lower_critical_solution_temp:
            self.is_recharging = False
            return "PHASE_OUT_BREATH: Exothermic event active. Hydrogel polymer network collapsing. Commencing passive evaporative cooling."
        
        elif core_temp_c < 35.0 and ambient_humidity_pct > 40.0:
            self.is_recharging = True
            return "PHASE_IN_BREATH: Computing idle. Casing temperature sub-threshold. Molecular air moisture absorption active."
        
        else:
            return "PHASE_STATIC: System thermal baseline stabilized. Air harvesting suspended."

if __name__ == "__main__":
    loop = HydrogelThermalLoop()
    # Test 1: Simulate intense cloud computing server workloads
    print(loop.evaluation_cycle(core_temp_c=58.4, ambient_humidity_pct=45.0))
    # Test 2: Simulate night-time standby mode recovery state
    print(loop.evaluation_cycle(core_temp_c=29.1, ambient_humidity_pct=62.0))
