#include <iostream>
#include<vector>
#include <math.h>
#include <map>
#include <algorithm>
#include <time.h>

#define numArgs 24

using namespace std;

class Object3D{
public:
    float x,y,z;
    Object3D(float x, float y, float z){
        this->x = x;
        this->y = y;
        this->z = z;
    }
    
    float distanceTo(Object3D v){
        return sqrt( (float)(this->x - v.x)*(this->x - v.x) + (float)(this->y - v.y)*(this->y - v.y) + (float)(this->z - v.z)*(this->z - v.z));
    }
    
    bool operator<(Object3D other) const
    {
        return this->x > other.x;
    }

    
};


Object3D finalPoint(vector<pair<float,Object3D> > pointList){
    float finalX = 0.0;
    float finalY = 0.0;
    float finalZ = 0.0;
    float weight = 0.0;
    for(int i=0; i < pointList.size()/2; i++){
        finalX += (pointList[i].second.x)*(1/pointList[i].first);
        finalY += (pointList[i].second.y)*(1/pointList[i].first);
        finalZ += (pointList[i].second.z)*(1/pointList[i].first);
        weight += 1/pointList[i].first;
    }
    Object3D final = Object3D( (finalX/weight), (finalY/weight), (finalZ/weight));
    return final;
}

vector<pair<float,Object3D> > multilateration_thread(vector<Object3D> SpeakersList, float iStart, float iStop, float jStart, float jStop, float kStart, float kStop, float distAB, float distBC, float distAC, float distAD, float distBD, float distCD ){
    vector<pair<float, Object3D> > fPointList;
    float stepIterationLength = 0.3;
    for(float i = iStart; i < iStop; i+=stepIterationLength){
        for(float j = jStart; j < jStop; j+=stepIterationLength){
            for(float k = kStart; k < kStop; k+=stepIterationLength){
                Object3D currentPoint(i,j,k);
                float distToSpeakerA = currentPoint.distanceTo(SpeakersList[0]);
                float distToSpeakerB = currentPoint.distanceTo(SpeakersList[1]);
                float distToSpeakerC = currentPoint.distanceTo(SpeakersList[2]);
                float distToSpeakerD = currentPoint.distanceTo(SpeakersList[3]);
                float testAB  = distToSpeakerA - distToSpeakerB;
                float testBC  = distToSpeakerB - distToSpeakerC;
                float testAC  = distToSpeakerA - distToSpeakerC;
                float testAD  = distToSpeakerA - distToSpeakerD;
                float testBD  = distToSpeakerB - distToSpeakerD;
                float testCD  = distToSpeakerC - distToSpeakerD;
                float accuracy = sqrt( ((distAB - testAB)*(distAB - testAB)) + ((distBC - testBC)*(distBC - testBC)) + ((distAC - testAC)*(distAC - testAC)) + ((distAD - testAD)*(distAD - testAD)) + ((distBD -  testBD)*(distBD -  testBD)) + ((distCD - testCD)*(distCD - testCD)) );
                //cout << accuracy << " " << currentPoint.x << currentPoint.y << currentPoint.z << endl;
                if (accuracy <= 1){
                    pair<float, Object3D> entry = make_pair(accuracy, currentPoint);
                    fPointList.push_back(entry);
                }
            }
        }
    }
    return fPointList;
}

int main(int argc, char *argv[]) {
    if (argc != numArgs){
        cout << "Wrong number of parameters!" << argc <<  endl;
        return -1;
    }
//    clock_t start =  clock();
    float speedOfSound = stof(argv[1]);
    Object3D SpeakerA(stof(argv[2]),stof(argv[3]),stof(argv[4]));
    Object3D SpeakerB(stof(argv[5]),stof(argv[6]),stof(argv[7]));
    Object3D SpeakerC(stof(argv[8]),stof(argv[9]),stof(argv[10]));
    Object3D SpeakerD(stof(argv[11]),stof(argv[12]),stof(argv[13]));
    vector<Object3D> SpeakersList;
    SpeakersList.push_back(SpeakerA);
    SpeakersList.push_back(SpeakerB);
    SpeakersList.push_back(SpeakerC);
    SpeakersList.push_back(SpeakerD);
    //Object3D target(stof(argv[14]), stof(argv[15]), stof(argv[16]));

    float timeA = stof(argv[14]);
    float timeB = stof(argv[15]);
    float timeC = stof(argv[16]);
    float timeD = stof(argv[17]);
    float timeAB = timeA - timeB;
    float timeBC = timeB - timeC;
    float timeAC = timeA - timeC;
    float timeAD = timeA - timeD;
    float timeBD = timeB - timeD;
    float timeCD = timeC - timeD;
    float distAB  = timeAB * speedOfSound;
    float distBC  = timeBC * speedOfSound;
    float distAC  = timeAC * speedOfSound;
    float distAD  = timeAD * speedOfSound;
    float distBD  = timeBD * speedOfSound;
    float distCD  = timeCD * speedOfSound;
    
    vector<pair<float, Object3D> > pointList = multilateration_thread(SpeakersList, stof(argv[18]), stof(argv[19]), stof(argv[20]), stof(argv[21]), stof(argv[22]), stof(argv[23]), distAB, distBC, distAC, distAD, distBD, distCD);

    sort(pointList.begin(), pointList.end());

    Object3D finalPointOut = finalPoint(pointList);
    
    cout << finalPointOut.x << " " << finalPointOut.y << " " << finalPointOut.z << endl;
//    double final = (clock() - start);
//    cout << final << " " << CLOCKS_PER_SEC <<  endl;
    
    
    return 0;
}
