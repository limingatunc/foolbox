import numpy as np

from foolbox.v1.attacks import LBFGSAttack as Attack


def test_attack(bn_adversarial):
    adv = bn_adversarial
    attack = Attack()
    attack(adv, num_random_targets=2)
    assert adv.perturbed is not None
    assert adv.distance.value < np.inf


def test_attack_with_init_attack(bn_adversarial):
    adv = bn_adversarial
    attack = Attack()
    attack(adv, num_random_targets=0)
    assert adv.perturbed is not None
    assert adv.distance.value < np.inf


def test_targeted_attack(bn_targeted_adversarial):
    adv = bn_targeted_adversarial
    attack = Attack()
    attack(adv)
    assert adv.perturbed is not None
    assert adv.distance.value < np.inf


def test_attack_gl(gl_bn_adversarial):
    adv = gl_bn_adversarial
    attack = Attack()
    attack(adv)
    assert adv.perturbed is None
    assert adv.distance.value == np.inf


def test_attack_pytorch(bn_adversarial_pytorch):
    adv = bn_adversarial_pytorch
    attack = Attack()
    attack(adv, num_random_targets=2)
    assert adv.perturbed is not None
    assert adv.distance.value < np.inf


def test_targeted_attack_pytorch(bn_targeted_adversarial_pytorch):
    adv = bn_targeted_adversarial_pytorch
    attack = Attack()
    attack(adv, num_random_targets=2)
    assert adv.perturbed is not None
    assert adv.distance.value < np.inf
