module TheBigThing
  def self.do_the_thing(lawyers_guns_and_money=nil)
    if not lawyers_guns_and_money
      raise "Send lawyers, guns or money!"
    end
    return true
  end
end
