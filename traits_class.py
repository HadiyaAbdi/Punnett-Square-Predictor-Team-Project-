class traits_class:
    """
    Represents a Mendelian genetic trait with one dominant and 
    one recessive allele. 
    
    This class stores allele symbols, phenotype 
    descriptions, and provides genotype validation and phenotype lookup.
    """
    
    def __init__ (self, name: str, alleles: list[str]):
        if len(alleles) != 2:
            raise ValueError("Traits must have exctly two alleles")

        self.name = name
        self.alleles = alleles
        self.dominant = {alleles[0]: True, alleles[1]: False}
        self.recessive = alleles[1]


    def get_name(self):
        return self.name
    def get_alleles(self):
        return self.alleles
    def get_dominant(self):
        return self.dominant
    def get_recessive(self):
        return self.recessive

    # Validate a genotype string (must be 2 characters, alleles must be valid)
    def validate_genotype(self, genotype: str) -> bool:
        if len(genotype) != 2:
            return False
        return all(allele in self.alleles for allele in genotype)
    
    # Convert genotype to phenotype
    def genotype_to_phenotype(self, genotype: str) -> str:
        if not self.validate_genotype(genotype):
            raise ValueError(f"Invalid genotype '{genotype}' for trait '{self.name}'")
        if self.dominant[genotype[0]] or self.dominant[genotype[1]]:
            return f"{self.name}: dominant expressed"
        else:
            return f"{self.name}: recessive expressed"
            