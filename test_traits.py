from ..Traits import Traits

def test_traits_class():
    print("Testing trait class")
    
    eye_color = Traits("Eye Color", ['G', 'g'])
    print("Trait name:", eye_color.get_name())
    print("Alleles:", eye_color.get_alleles())

    # Test 3: Validate valid genotypes
    print("Is 'Bb' valid?", eye_color.validate_genotype("Gg"))
    print("Is 'bb' valid?", eye_color.validate_genotype("gg"))

    # Test 4: Validate invalid genotype
    print("Is 'BBB' valid?", eye_color.validate_genotype("GGG"))
    print("Is 'Xb' valid?", eye_color.validate_genotype("Xg"))

    # Test 5: Genotype → phenotype conversion
    print("Phenotype for 'BB':", eye_color.genotype_to_phenotype("GG"))
    print("Phenotype for 'Bb':", eye_color.genotype_to_phenotype("Gg"))
    print("Phenotype for 'bb':", eye_color.genotype_to_phenotype("gg"))

if __name__ == "__main__":
    test_traits_class()