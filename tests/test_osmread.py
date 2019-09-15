import pyroutelib3

def test_osmread():

    print(pyroutelib3.__version__)

    assert pyroutelib3.OSMREAD_AVAILABLE == True, "osmread has to be installed for testing"

    etree_ds = pyroutelib3.Datastore("car", "tests/test_mikolajki.osm", use_osmread=False)
    osmrd_ds = pyroutelib3.Datastore("car", "tests/test_mikolajki.osm", use_osmread=True)

    assert etree_ds.rnodes == osmrd_ds.rnodes
    assert etree_ds.routing == osmrd_ds.routing
    assert etree_ds.mandatoryMoves == osmrd_ds.mandatoryMoves
    assert etree_ds.forbiddenMoves == osmrd_ds.forbiddenMoves
