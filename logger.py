class Logger(object):

    def __init__(self, file_name):
      self.file_name = file_name
      # print('logger init!')

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate):
      log = open(self.file_name, "w")
      log.write(f"Virus: {virus_name}, Population: {pop_size}, Percent Vaccinated:{vacc_percentage}, Mortality Rate: {mortality_rate}, Reproduction Rate: {repro_rate}\n\n")
      log.close()

    def log_step(self, alive, infected, died, step, vacc_percent):
      log = open(self.file_name, 'a')
      log.write(f"Step: {step}\nAlive: {alive}\nDead: {died}\nInfected: {infected}\nVaccinated: {vacc_percent}\n\n")
      log.close()


# ----------------------------------------------------------------------- #

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        log = open(self.file_name, "a")
        if did_infect:
          log.write(f"{person._id} infects {random_person._id} \n")
        else:
          if random_person_sick:
            log.write(f"{person._id} didn't infect {random_person._id} because they were already sick.\n")
          else:
            log.write(f"{person._id} didn't infect {random_person._id} because they are vaccinated.\n")
        log.close()


    def log_infection_survival(self, person, did_die_from_infection):
      log = open(self.file_name, "a")
      if did_die_from_infection:
         log.write(f"{person._id} died from infection.\n")
      else:
        log.write(f"{person._id} survived the infection.\n")
      log.close()






    def log_time_step(self, time_step_number):
  
        pass
